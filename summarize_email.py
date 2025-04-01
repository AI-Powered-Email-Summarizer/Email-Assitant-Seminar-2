#used to summarize emails
import google.generativeai as genai
import streamlit as st

genai.configure(api_key="API-key")

@st.cache_data(ttl=600)
def summarize_email(subject):
    model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp")
    prompt = f"Summarize this email:\n\nSubject: {subject}"
    response = model.generate_content(prompt)
    return response.text.strip() if response else "No summary available."
