import re

import streamlit as st 
import requests

WEBHOOK_URL = "https://connect.pabbly.com/workflow/sendwebhookdata/IjU3NjYwNTZjMDYzMDA0MzY1MjY5NTUzNTUxMzMi_pc"

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
            # st.success("Message succesfully sent!")
            # st.success("Thank you for your message! I will get back to you soon.")
            if not WEBHOOK_URL:
                st.error("Email service is not set up. Please try again.", icon=":material/contact_mail:")
                st.stop()
            
            if not name:
                st.error("Please provide your name.", icon=":material/face:")
                st.stop()
            
            if not email:
                st.error("Please provide your email address.", icon=":material/mail_off:")
                st.stop()
            
            if not is_valid_email(email):
                st.error("Please provide a valid email address.", icon=":material/mail:")
                st.stop()
            
            if not message:
                st.error("Please provide a message.", icon=":material/forum:")
                st.stop()
            
            # prepare the data payload and sent it to the specified webhook URL
            data = {"email": email, "name": name, "message": message}
            response = requests.post(WEBHOOK_URL, json=data)
            
            if response.status_code == 200:
                st.success("Your message has been sent succesfully! :material/celebration:", icon=":material/cake:")
            else:
                st.error("There was an error sending your message. Please try again.", icon=":material/bug_report")
            