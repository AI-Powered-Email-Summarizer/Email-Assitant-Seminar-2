import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from authenticate import authenticate_gmail_api
import streamlit as st

def create_message(sender, to, subject, message_text):
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject
    msg = MIMEText(message_text)
    message.attach(msg)
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
    return {'raw': raw_message}

def send_email(sender, to, subject, message_text):
    service = authenticate_gmail_api()
    email_message = create_message(sender, to, subject, message_text)

    try:
        service.users().messages().send(userId="me", body=email_message).execute()
        return "✅ Reply Sent!"
    except Exception as e:
        return f"Error sending email: {e}"
