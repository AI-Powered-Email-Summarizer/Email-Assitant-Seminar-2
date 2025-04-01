#used in classification of emails
import google.generativeai as genai
import streamlit as st

genai.configure(api_key="API-key")

@st.cache_data(ttl=600)
def classify_email(subject):
    model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp")
    prompt = f"Classify this email into one of these categories: Work, Personal, Promotion, Spam, Other.\n\nSubject: {subject}"
    response = model.generate_content(prompt)
    return response.text.strip() if response else "Other"
