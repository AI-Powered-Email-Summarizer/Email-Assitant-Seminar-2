#used to fetch unread Emails
from authenticate import authenticate_gmail_api
import streamlit as st

@st.cache_data(ttl=300)
def get_unread_emails():
    service = authenticate_gmail_api()
    results = service.users().messages().list(userId="me", labelIds=["INBOX"], q="is:unread", maxResults=20).execute()
    messages = results.get("messages", [])

    email_list = []
    for message in messages:
        msg = service.users().messages().get(userId="me", id=message["id"], format="metadata").execute()
        headers = msg["payload"]["headers"]

        subject = next((header["value"] for header in headers if header["name"] == "Subject"), "No Subject")
        sender = next((header["value"] for header in headers if header["name"] == "From"), "Unknown Sender")

        if "mailer-daemon@googlemail.com" not in sender.lower():
            email_list.append({"id": message["id"], "subject": subject, "sender": sender})

    return email_list
