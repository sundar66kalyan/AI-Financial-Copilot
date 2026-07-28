import streamlit as st
import requests

from config import LOGIN_URL


def login():

    st.title("🔐 Login")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

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

            st.success("Login Successful")
            st.switch_page("pages/1_Dashboard.py")

        else:

            st.error("Invalid Credentials")