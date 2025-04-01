📧 AI-Powered Email Assistant
This project uses Google Gemini AI and the Gmail API to classify, summarize, and auto-reply to emails using Streamlit.

🚀 Features
✅ Fetch unread emails from Gmail
✅ Classify emails into categories (Work, Personal, Spam, etc.)
✅ Summarize emails automatically
✅ Generate AI-powered email replies
✅ Send replies directly from the UI

🛠 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-repo/email-assistant.git
cd email-assistant
2️⃣ Create a Virtual Environment
bash
Copy
Edit
python -m venv venv
Activate the virtual environment:

Windows:

bash
Copy
Edit
venv\Scripts\activate
Mac/Linux:

bash
Copy
Edit
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
4️⃣ Setup Google API Credentials
Go to Google Cloud Console

Enable the Gmail API

Download credentials.json and place it in the project folder

5️⃣ Configure Google Gemini API
Sign up at Google AI Studio

Get an API Key and update it in generate_reply.py, summarize_email.py, and classify_email.py:

python
Copy
Edit
genai.configure(api_key="YOUR_GEMINI_API_KEY")
▶️ Running the Project
bash
Copy
Edit
streamlit run main.py
📌 Usage
Select an unread email from the list.

Choose an action:

Classify: Categorizes the email.

Summarize: Provides a brief summary.

Auto-reply: Generates a response using AI.

If replying, review the generated response and click Send Reply.
