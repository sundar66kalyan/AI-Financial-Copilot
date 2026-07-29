import streamlit as st
import requests

from config import (
    SPENDING_URL,
    HEALTH_URL,
    BACKEND_URL,
)

st.set_page_config(
    page_title="Analytics",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Financial Analytics")

token = st.session_state.get("access_token")

if not token:
    st.warning("Please login first.")
    st.stop()

headers = {
    "Authorization": f"Bearer {token}"
}

# =====================================================
# Spending Summary
# =====================================================

st.subheader("💰 Spending Summary")

try:

    response = requests.get(
        SPENDING_URL,
        headers=headers,
        timeout=10
    )

    if response.status_code == 200:

        data = response.json()

        income = data.get("total_income", 0)
        expense = data.get("total_expense", 0)
        balance = data.get("net_balance", 0)

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
            "💰 Balance",
            f"${balance:,.2f}"
        )

        st.divider()

        st.subheader("📂 Expense by Category")

        expense_category = data.get(
            "expense_by_category",
            {}
        )

        if expense_category:
            st.json(expense_category)
        else:
            st.info("No expense categories available.")

    else:
        st.error(response.text)

except Exception as e:
    st.error(str(e))

# =====================================================
# Financial Health
# =====================================================

st.divider()

st.subheader("❤️ Financial Health")

try:

    response = requests.get(
        HEALTH_URL,
        headers=headers,
        timeout=10
    )

    if response.status_code == 200:

        health = response.json()

        score = health.get("score", 0)

        status = health.get(
            "status",
            "Unknown"
        )

        st.metric(
            "Financial Health Score",
            f"{score}/100"
        )

        if score >= 80:
            st.success(status)

        elif score >= 50:
            st.warning(status)

        else:
            st.error(status)

    else:
        st.error(response.text)

except Exception as e:
    st.error(str(e))

# =====================================================
# AI Insights
# =====================================================

st.divider()

st.subheader("🤖 AI Insights")

try:

    response = requests.get(
        f"{BACKEND_URL}/api/v1/insights/",
        headers=headers,
        timeout=15
    )

    if response.status_code == 200:

        insights = response.json()["insights"]

        for item in insights:
            st.success(item)

    else:

        st.warning(
            "Unable to load AI Insights."
        )

except Exception:

    st.warning(
        "AI Insights service unavailable."
    )