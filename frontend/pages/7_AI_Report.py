import os
import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="AI Financial Report",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Financial Report")

st.caption(
    "Generate a professional AI-powered financial report based on your accounts, transactions, budgets and analytics."
)

# -------------------------------------------------------
# Login Check
# -------------------------------------------------------

if "access_token" not in st.session_state:
    st.warning("Please login first.")
    st.stop()

headers = {
    "Authorization": f"Bearer {st.session_state['access_token']}"
}

# -------------------------------------------------------
# Generate Report
# -------------------------------------------------------

if st.button(
    "📄 Generate Financial Report",
    use_container_width=True
):

    with st.spinner("Generating AI Financial Report..."):

        try:

            response = requests.get(
                f"{API_URL}/api/v1/report/generate",
                headers=headers,
                timeout=120
            )

            if response.status_code == 200:

                data = response.json()

                st.success("✅ AI Financial Report generated successfully.")

                st.divider()

                st.subheader("📊 Financial Report")

                with st.expander(
                    "View Report",
                    expanded=True
                ):
                    st.markdown(data["report"])

                pdf_file = data.get("pdf")

                if pdf_file and os.path.exists(pdf_file):

                    with open(pdf_file, "rb") as file:

                        st.download_button(
                            label="📥 Download PDF Report",
                            data=file,
                            file_name="financial_report.pdf",
                            mime="application/pdf",
                            use_container_width=True
                        )

                else:

                    st.info("PDF file is not available.")

            else:

                st.error(
                    f"API Error ({response.status_code})"
                )

        except Exception as e:

            st.error(str(e))