﻿# 🤖 HR Assistant Chatbot

## 📌 Overview
The **HR Assistant Chatbot** is an AI-powered HR virtual assistant designed to provide instant responses to HR-related queries. It utilizes **FAISS** for efficient search, **GPT-based AI** for intelligent responses, and **Gradio** for an interactive UI. The chatbot also supports **multilingual translations** and **theme customization**.

## 🚀 Features
- ✅ **Instant AI-powered HR responses**
- ✅ **Multilingual Support** (Translate chatbot responses)
- ✅ **Light/Dark Theme Toggle**
- ✅ **Predefined HR Questions for quick access**
- ✅ **FAISS Vector Store for efficient search**
- ✅ **Gradio-based User Interface**
- ✅ **Secure API Key Handling using `.env`**

## 🏗️ Project Structure
```
HR_Chatbot/
│── .env                # API Keys and Configurations (keep this secret)
│── main.py             # Main chatbot application
│── document_loader.py  # Loads and processes HR policy PDFs
│── vector_store.py     # Converts text to embeddings & stores them in FAISS
│── chatbot.py          # Chatbot logic (query processing & response generation)
│── ui.py               # Gradio UI
│── requirements.txt    # List of dependencies for easy installation
│── README.md           # Project description & setup guide
│── data/
│   ├── hr_policies.pdf # HR policy document
│── models/
│   ├── faiss_index     # Vector database
```

## 🛠️ Installation & Setup

### 1️⃣ Clone the repository
```sh
git clone https://github.com/udaybhadauria/HR_Chatbot.git
cd HR_Chatbot
```

### 2️⃣ Create a virtual environment (recommended)
```sh
python -m venv venv
source venv/bin/activate  # On Mac/Linux
venv\Scripts\activate     # On Windows
```

### 3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Set up environment variables
Create a `.env` file in the root directory and add your **API keys** (e.g., OpenAI API Key):
```
OPENAI_API_KEY=your_openai_api_key
```

### 5️⃣ Load HR policies and generate vector store
```sh
python document_loader.py
python vector_store.py
```

### 6️⃣ Run the chatbot
```sh
python main.py
```

## 📜 Technologies Used
- **Python 3.10+**
- **Gradio** (for UI)
- **FAISS** (for vector database)
- **OpenAI GPT API** (for chatbot responses)
- **Deep Translator** (for multilingual support)
- **dotenv** (for environment variable management)

## 🌐 Deployment (Optional)
Deploy your chatbot to **Hugging Face Spaces** using Gradio:
```sh
gradio deploy
```

## 📩 Contact
For any questions, contact **[Uday Bhadauria](mailto:bhadauria.uday@gmail.com)**  
**GitHub:** [udaybhadauria](https://github.com/udaybhadauria)


