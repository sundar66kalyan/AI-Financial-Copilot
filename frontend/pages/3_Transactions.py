import streamlit as st
import requests
import pandas as pd

from config import TRANSACTION_URL, ACCOUNT_URL, CATEGORY_URL

st.title("💰 Transactions")

token = st.session_state.get("access_token")

if not token:
    st.warning("Please login first.")
    st.stop()

headers = {
    "Authorization": f"Bearer {token}"
}

# -------------------------------------------------
# Load Accounts & Categories
# -------------------------------------------------

accounts = requests.get(
    ACCOUNT_URL,
    headers=headers
).json()

categories = requests.get(
    CATEGORY_URL,
    headers=headers
).json()

# -------------------------------------------------
# Add Transaction
# -------------------------------------------------

with st.expander("➕ Add New Transaction", expanded=True):

    if len(accounts) == 0:
        st.info("Create an account first.")
        st.stop()

    if len(categories) == 0:
        st.info("Create a category first.")
        st.stop()

    account = st.selectbox(
        "Account",
        accounts,
        format_func=lambda x: x["name"]
    )

    category = st.selectbox(
        "Category",
        categories,
        format_func=lambda x: x["name"]
    )

    title = st.text_input("Title")

    amount = st.number_input(
        "Amount",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

    transaction_type = st.selectbox(
        "Transaction Type",
        ["Income", "Expense"]
    )

    description = st.text_input("Description")

    if st.button(
        "Add Transaction",
        use_container_width=True
    ):

        if not title.strip():
            st.error("Please enter a title.")
            st.stop()

        payload = {
            "title": title,
            "account_id": account["id"],
            "category_id": category["id"],
            "amount": amount,
            "transaction_type": transaction_type,
            "description": description,
        }

        response = requests.post(
            TRANSACTION_URL,
            headers=headers,
            json=payload
        )

        if response.status_code in [200, 201]:
            st.success("✅ Transaction added successfully.")
            st.rerun()
        else:
            st.error(response.text)

st.divider()

# -------------------------------------------------
# Transactions
# -------------------------------------------------

response = requests.get(
    TRANSACTION_URL,
    headers=headers
)

if response.status_code != 200:
    st.error("Unable to load transactions.")
    st.stop()

transactions = response.json()

income = sum(
    float(t["amount"])
    for t in transactions
    if t["transaction_type"] == "Income"
)

expense = sum(
    float(t["amount"])
    for t in transactions
    if t["transaction_type"] == "Expense"
)

balance = income - expense

c1, c2, c3 = st.columns(3)

c1.metric(
    "💵 Income",
    f"${income:,.2f}"
)

c2.metric(
    "💸 Expense",
    f"${expense:,.2f}"
)

c3.metric(
    "💰 Net Balance",
    f"${balance:,.2f}"
)

st.divider()

st.subheader("📋 Transaction History")

if len(transactions) == 0:
    st.info("No transactions found.")
else:
    st.dataframe(
        pd.DataFrame(transactions),
        use_container_width=True,
        hide_index=True
    )