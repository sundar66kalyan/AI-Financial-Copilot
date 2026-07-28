import streamlit as st
import requests

from config import LOGIN_URL

st.title("🔐 Login")

email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Login"):

    response = requests.post(
        LOGIN_URL,
        data={
            "username": email,
            "password": password
        }
    )

    if response.status_code == 200:

        token = response.json()["access_token"]

        st.session_state["access_token"] = token
        st.session_state["logged_in"] = True

        st.success("Login Successful ✅")
        st.switch_page("pages/1_Dashboard.py")

    else:

        st.error("Invalid Email or Password")

st.divider()

st.subheader("🚀 Demo Account")

st.info("""
**Email:** sundar@example.com

**Password:** Password123
""")

st.subheader("📌 About This Application")

st.write("""
AI Financial Copilot is an AI-powered personal finance management platform that helps users:

• Manage financial accounts

• Track income and expenses

• Create monthly budgets

• Analyze financial health

• Generate AI-powered financial reports

• Receive personalized financial recommendations using Google Gemini AI.
""")

st.subheader("📖 How to Use")

st.markdown("""
1. Login using the demo account.

2. View your Dashboard.

3. Manage Accounts.

4. Add Income & Expense Transactions.

5. Create Budgets.

6. Explore Analytics & AI Insights.

7. Ask questions using AI Financial Copilot.

8. Generate AI Financial Reports.
""")

st.subheader("✨ Features")

st.markdown("""
- 🔐 JWT Authentication

- 💳 Account Management

- 💸 Transaction Tracking

- 📊 Budget Management

- 📈 Spending Analytics

- ❤️ Financial Health Analysis

- 🤖 AI Financial Copilot

- 📄 AI Financial Reports (PDF)

- 💡 AI Insights

- ⚡ FastAPI REST APIs

- 🖥️ Streamlit Dashboard
""")

st.divider()

st.caption("""
Developed by

👨‍💻 **Kalyana Sundar**

**AI Engineer**

© 2026 AI Financial Copilot
""")