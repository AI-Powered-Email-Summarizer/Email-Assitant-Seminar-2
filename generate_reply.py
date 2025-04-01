#generates Reply using AI
import google.generativeai as genai
import streamlit as st

genai.configure(api_key="AIzaSyBZtr2XaK-V1M4xxUZiglhLoLKgUo6IMhQ")

@st.cache_data(ttl=600)
def generate_ai_response(subject):
    model = genai.GenerativeModel("gemini-2.0-flash-thinking-exp")
    prompt = f"Generate a short professional reply for an email with this subject: {subject}"
    response = model.generate_content(prompt)
    return response.text if response else "Sorry, I couldn't generate a response."
