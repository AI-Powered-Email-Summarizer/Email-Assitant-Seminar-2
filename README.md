# 📧 AI-Powered Email Assistant

This project uses **Google Gemini AI** and the **Gmail API** to classify, summarize, and auto-reply to emails using **Streamlit**.

## 🚀 Features
- ✅ Fetch unread emails from Gmail
- ✅ Classify emails into categories (Work, Personal, Spam, etc.)
- ✅ Summarize emails automatically
- ✅ Generate AI-powered email replies
- ✅ Send replies directly from the UI

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/email-assistant.git
cd email-assistant
```

### 2️⃣ Create a Virtual Environment
```bash
python -m venv venv
```
Activate the virtual environment:

#### Windows:
```bash
venv\Scripts\activate
```
#### Mac/Linux:
```bash
source venv/bin/activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Setup Google API Credentials
- Go to **Google Cloud Console**
- Enable the **Gmail API**
- Download `credentials.json` and place it in the project folder

### 5️⃣ Configure Google Gemini API
- Sign up at **Google AI Studio**
- Get an **API Key** and update it in `generate_reply.py`, `summarize_email.py`, and `classify_email.py`:

```python
import genai

genai.configure(api_key="YOUR_GEMINI_API_KEY")
```

---

## ▶️ Running the Project
```bash
streamlit run main.py
```

---

## 📌 Usage
1. Select an unread email from the list.
2. Choose an action:
   - **Classify**: Categorizes the email.
   - **Summarize**: Provides a brief summary.
   - **Auto-reply**: Generates a response using AI.
3. If replying, review the generated response and click **Send Reply**.
