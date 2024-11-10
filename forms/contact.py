import re

import streamlit as st 
import requests

WEBHOOK_URL = ""

def is_valid_email(email):
    # Basic regex pattern for email validation
    email_pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-.]+$"
    return re.match(email_pattern, email) is not None

def contact_form():
    with st.form("contact_form"):
        name = st.text_input("First Name")
        email = st.text_input("Email Address")
        message = st.text_area("Your Message")
        submit_btn = st.form_submit_button("Submit")
        
        if submit_btn:
            st.success("Message succesfully sent!")
            # st.success("Thank you for your message! I will get back to you soon.")