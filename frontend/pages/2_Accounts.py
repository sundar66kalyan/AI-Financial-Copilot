import streamlit as st
import requests
import pandas as pd

from config import ACCOUNT_URL

st.title("💳 Accounts")

token = st.session_state.get("access_token")

if not token:
    st.warning("Please login first.")
    st.stop()

headers = {
    "Authorization": f"Bearer {token}"
}

# ----------------------------
# Create Account
# ----------------------------

with st.expander("➕ Create New Account", expanded=True):

    name = st.text_input("Account Name")

    account_type = st.selectbox(
        "Account Type",
        [
            "Savings",
            "Checking",
            "Credit Card",
            "Investment"
        ]
    )

    balance = st.number_input(
        "Opening Balance",
        min_value=0.0,
        value=0.0,
        step=100.0
    )

    if st.button("Create Account", use_container_width=True):

        response = requests.post(
            ACCOUNT_URL,
            headers=headers,
            json={
                "name": name,
                "account_type": account_type,
                "balance": balance
            }
        )

        if response.status_code in [200, 201]:
            st.success("✅ Account created successfully.")
            st.rerun()
        else:
            st.error(response.text)

st.divider()

# ----------------------------
# Load Accounts
# ----------------------------

response = requests.get(
    ACCOUNT_URL,
    headers=headers
)

if response.status_code != 200:
    st.error("Unable to load accounts.")
    st.stop()

accounts = response.json()

# ----------------------------
# Summary
# ----------------------------

total_accounts = len(accounts)

total_balance = sum(
    float(account.get("balance", 0))
    for account in accounts
)

col1, col2 = st.columns(2)

col1.metric(
    "💳 Total Accounts",
    total_accounts
)

col2.metric(
    "💰 Total Balance",
    f"₹{total_balance:,.2f}"
)

st.divider()

# ----------------------------
# Accounts Table
# ----------------------------

st.subheader("📋 My Accounts")

if not accounts:
    st.info("No accounts found.")
else:
    st.dataframe(
        pd.DataFrame(accounts),
        use_container_width=True,
        hide_index=True
    )