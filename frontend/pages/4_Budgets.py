import streamlit as st
import requests
import pandas as pd

from config import BUDGET_URL, CATEGORY_URL

st.title("💰 Budget Management")

token = st.session_state.get("access_token")

if not token:
    st.warning("Please login first.")
    st.stop()

headers = {
    "Authorization": f"Bearer {token}"
}

# -----------------------------
# Load Categories
# -----------------------------
categories = requests.get(
    CATEGORY_URL,
    headers=headers
).json()

if len(categories) == 0:
    st.info("Create a category first.")
    st.stop()

# -----------------------------
# Create Budget
# -----------------------------
with st.expander("➕ Create New Budget", expanded=True):

    category = st.selectbox(
        "Category",
        categories,
        format_func=lambda x: x["name"]
    )

    amount = st.number_input(
        "Budget Amount",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

    name = st.text_input(
        "Budget Name",
        "Monthly Budget"
    )

    month = st.selectbox(
        "Month",
        [
            "January","February","March","April","May","June",
            "July","August","September","October","November","December"
        ]
    )

    year = st.number_input(
        "Year",
        min_value=2024,
        max_value=2100,
        value=2026
    )

    if st.button(
        "Create Budget",
        use_container_width=True
    ):

        payload = {
            "name": name,
            "category_id": category["id"],
            "amount": amount,
            "month": month,
            "year": int(year)
        }

        response = requests.post(
            BUDGET_URL,
            headers=headers,
            json=payload
        )

        if response.status_code in [200, 201]:
            st.success("✅ Budget created successfully.")
            st.rerun()
        else:
            st.error(response.text)

st.divider()

# -----------------------------
# Load Budgets
# -----------------------------
response = requests.get(
    BUDGET_URL,
    headers=headers
)

if response.status_code != 200:
    st.error("Unable to load budgets.")
    st.stop()

budgets = response.json()

# -----------------------------
# Summary Cards
# -----------------------------
total_budgets = len(budgets)

total_budget_amount = sum(
    float(budget.get("amount", 0))
    for budget in budgets
)

col1, col2 = st.columns(2)

col1.metric(
    "📊 Total Budgets",
    total_budgets
)

col2.metric(
    "💰 Total Budget Amount",
    f"${total_budget_amount:,.2f}"
)

st.divider()

# -----------------------------
# Budget Table
# -----------------------------
st.subheader("📋 Budget List")

if len(budgets) == 0:
    st.info("No budgets found.")
else:
    st.dataframe(
        pd.DataFrame(budgets),
        use_container_width=True,
        hide_index=True
    )