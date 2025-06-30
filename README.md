# 🧠 GenAI Multi-Modal App

Your all-in-one AI-powered tool for **summarization**, **generation**, and **assistant tasks**, built using **Python**, **Streamlit**, and **OpenAI APIs**.

(static/logo.jpg)

---

## 🚀 Features

### 📝 Summarizer Tool
- **Text Summarizer**: Paste raw text and get a clean summary.
- **YouTube Summarizer**: Extract and summarize video captions from any YouTube link.
- **Article Summarizer**: Summarize online articles using their URLs.
- **PDF/DOCX Summarizer**: Upload documents and receive concise summaries.

### ✨ Generator Tool
- **Text-to-Code**: Generate Python code from natural language prompts.
- **Text-to-Speech**: Convert text into realistic audio using AI voices.
- **Text-to-Image**: Generate images based on user prompts.
- **YouTube Caption Generator**: Automatically generate captions for uploaded videos.

### 💬 Assistant Tool
- **Document QnA**: Ask questions from uploaded PDFs.
- **URL QnA**: Ask questions based on the content of a web page.

---

## 📂 Project Structure
```bash
.
├── .streamlit/
│ └── config.toml
├── Assistant/
│ ├── assistant_app.py
│ ├── document_qna.py
│ ├── url_qna.py
│ └── ...
├── Generator/
│ ├── generator_app.py
│ ├── image_gen.py
│ ├── text_to_code.py
│ ├── text_to_speech.py
│ └── yt_caption_generator.py
├── Summarizer/
│ ├── article_summarizer.py
│ ├── file_summarizer.py
│ ├── Summarizer_app.py
│ └── YT_summary.py
├── static/
│ └── logo.jpg
├── main.py
├── requirements.txt
└── .env

```
---

## 🛠️ Setup & Installation

### 🔹 Clone the repo

```bash
git clone https://github.com/YOUR_USERNAME/ai-multimodal-app.git
cd ai-multimodal-app

🔹 Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # or venv\Scripts\activate on Windows

🔹 Install dependencies

pip install -r requirements.txt

🔹 Add your API keys

Create a .env file and add:

OPENAI_API_KEY=your_openai_key
HF_TOKEN=your_huggingface_token

▶️ Running the App Locally

streamlit run main.py

☁️ Deployment on Streamlit Cloud

    Push the project to GitHub.

    Visit: https://streamlit.io/cloud

    Log in with GitHub and click "New app".

    Select your repo and set main.py as the entry point.

    Click Deploy — that’s it!

📸 Screenshots

<!-- Replace with actual image path if desired -->
🙌 Acknowledgements

    OpenAI

    Hugging Face

    Streamlit

    YouTube Transcript API & BeautifulSoup for scraping

📬 Contact

Maintained by Archit Kumar
GitHub: @Lamstersickness
