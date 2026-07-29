import streamlit as st
import requests

from config import COPILOT_URL

st.set_page_config(
    page_title="AI Financial Copilot",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Financial Copilot")
st.caption("Ask AI about budgeting, savings, investments, expenses, and your financial health.")

# -------------------------------------------------
# Login Check
# -------------------------------------------------

if "access_token" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

headers = {
    "Authorization": f"Bearer {st.session_state['access_token']}"
}

# -------------------------------------------------
# Chat History
# -------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# -------------------------------------------------
# User Input
# -------------------------------------------------

prompt = st.chat_input("Ask your financial question...")

if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("🤖 AI is analyzing your financial data..."):

        try:

            response = requests.post(
                COPILOT_URL,
                headers=headers,
                json={
                    "question": prompt
                },
                timeout=60
            )

            if response.status_code == 200:

                answer = response.json().get(
                    "answer",
                    "No response received."
                )

            else:

                answer = f"❌ API Error ({response.status_code})"

        except Exception as e:

            answer = f"❌ {str(e)}"

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

# -------------------------------------------------
# Clear Chat
# -------------------------------------------------

st.divider()

if st.button("🗑️ Clear Chat History"):

    st.session_state.messages = []

    st.rerun()