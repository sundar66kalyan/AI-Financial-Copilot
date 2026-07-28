import streamlit as st
import requests
import pandas as pd

from config import (
    ACCOUNT_URL,
    TRANSACTION_URL,
    BUDGET_URL,
)

st.title("📊 Dashboard")

token = st.session_state.get("access_token")

if not token:
    st.warning("Please login first.")
    st.stop()

headers = {
    "Authorization": f"Bearer {token}"
}

# ----------------------------
# Load Data
# ----------------------------
accounts = requests.get(ACCOUNT_URL, headers=headers).json()
transactions = requests.get(TRANSACTION_URL, headers=headers).json()
budgets = requests.get(BUDGET_URL, headers=headers).json()

# ----------------------------
# KPI Cards
# ----------------------------

total_accounts = len(accounts)
total_transactions = len(transactions)
total_budgets = len(budgets)

balance = 0

for account in accounts:
    balance += float(account.get("balance", 0))

col1, col2, col3, col4 = st.columns(4)

col1.metric("💳 Accounts", total_accounts)
col2.metric("💸 Transactions", total_transactions)
col3.metric("📊 Budgets", total_budgets)
col4.metric("💰 Total Balance", f"₹{balance:,.2f}")

st.divider()

# ----------------------------
# Accounts
# ----------------------------

st.subheader("💳 Accounts")

if accounts:
    st.dataframe(
        pd.DataFrame(accounts),
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("No accounts found.")

st.divider()

# ----------------------------
# Recent Transactions
# ----------------------------

st.subheader("💸 Recent Transactions")

if transactions:
    st.dataframe(
        pd.DataFrame(transactions),
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("No transactions available.")

st.divider()

# ----------------------------
# Budgets
# ----------------------------

st.subheader("📊 Budgets")

if budgets:
    st.dataframe(
        pd.DataFrame(budgets),
        use_container_width=True,
        hide_index=True,
    )
else:
    st.info("No budgets available.")