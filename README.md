# 🌟 AI-HUB — Your One-Stop AI Assistant Platform

AI-HUB is a powerful, modern, and responsive web application built with **React** (frontend) and **Django** (backend). Leveraging advanced **Generative AI** tools and NLP capabilities, AI-HUB enables users to interact with multiple smart tools in one place — from YouTube Q&A to PDF chat, summarization, currency conversion, and even weather tracking!

---

## 🚀 Features

1. 🎥 **YouTube Q&A**
   - Paste a YouTube video link
   - Extracts transcript
   - Ask any question about the video content

2. 📚 **Text Summarization**
   - Paste any long text chunk
   - Choose from multiple summarization contexts (e.g. concise, bullet points, casual, academic)

3. 📄 **Chat with Your PDF**
   - Upload a PDF document
   - Ask anything about it — instant answers using RAG and vector-based search

4. 💱 **Currency Converter**
   - Real-time exchange rates
   - Clean and simple UI inspired by Google currency converter

5. 🌤️ **Weather Checker**
   - Get live weather updates
   - City-based search with temperature, conditions, and more

---

## 🧠 Tech Stack

### 💻 Frontend
- React.js
- Tailwind CSS (or any styling framework of your choice)
- Axios / Fetch for API communication

### 🧠 Backend
- Django + Django REST Framework
- LangChain (LLM Orchestration)
- OpenAI / Gemini (for LLM support)
- PyPDF2 / pdfminer.six for PDF parsing
- Wikipedia, MMR, and MQR-based retrievers
- Vector Stores: FAISS / Pinecone
- Text Splitters: Recursive & Standard
- Custom agents & prompt templates

---

## 📦 AI Concepts Used (Warmup & Project Work)

- **Parsers**: Pydantic, JSON, Chain, String, Structured
- **Runnables**: Branch, Lambda, Parallel, Sequence, Passthrough
- **Chains**: SequentialChain, SimpleChain, ConditionalChain, ParallelChain
- **Embeddings & Vector Stores**: FAISS, Pinecone
- **Retrievers**: MMRRetriever, MQRRetriever, WikipediaRetriever, VectorStoreRetriever
- **Text Splitters**: RecursiveCharacterTextSplitter, CharacterTextSplitter
- **RAG Concept**: Retrieval-Augmented Generation
- **Agents**: LLM agent, Tool calling, Prompt Engineering

---

## 📸 Preview

![Screenshot 2025-06-10 081532](https://github.com/user-attachments/assets/f1d3ba19-da8a-4942-ac99-892c8c4da041)
![Screenshot 2025-06-10 061931](https://github.com/user-attachments/assets/512375a5-9481-480e-8dec-46f17924d512)
![Screenshot 2025-06-10 065936](https://github.com/user-attachments/assets/65fee116-d838-4d1d-ab5c-3e56dc73f4f1)
![Screenshot 2025-06-10 061606](https://github.com/user-attachments/assets/248c4522-8252-4908-8037-799b09090827)
![Screenshot 2025-06-10 061639](https://github.com/user-attachments/assets/21857001-37ea-4e74-aac4-ec3797eba6db)
![Screenshot 2025-06-10 061228](https://github.com/user-attachments/assets/947b74c3-10f1-4f79-a62a-513797c6c7c6)
![Screenshot 2025-06-10 061215](https://github.com/user-attachments/assets/0b637ec3-92cd-4913-9f02-7e8b4ca4a563)
![Screenshot 2025-06-10 070129](https://github.com/user-attachments/assets/fd271714-32e1-4d41-8ed9-89855179be8c)
![Screenshot 2025-06-10 070120](https://github.com/user-attachments/assets/1c14c301-9f29-460b-8334-e108564a9d67)
![Screenshot 2025-06-10 070210](https://github.com/user-attachments/assets/5f4f77f5-3a29-4e4c-a2f4-4a6f95eb618f)
![Screenshot 2025-06-10 070232](https://github.com/user-attachments/assets/b77acbd8-22fc-4fba-8209-7aedbf67f657)





---

## ⚙️ Setup Instructions

1. **Clone the repo**
   ```bash
   git clone https://github.com/souravdebnath109/AI_HUB.git


##  Backend Setup
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
``` 


##  Frontend Setup
```bash
cd frontend
npm install
npm start
``` 
##  📚 Learning Journey

This project was built after completing the YouTube GenAI Course:
```bash
https://www.youtube.com/watch?v=pSVk-5WemQ0&list=PLKnIA16_RmvaTbihpo4MtzVm4XOQa0ER0
```

##  🛠 Future Improvements

- **Add user authentication**
- **Store chat history and upload history**
- **Support for multilingual queries**
- **Voice-to-text integration**
- **Voice-to-text integration**

##  🙌 Author
- **Contact**  : souravdebnath54474@gmail.com
- **Linkedin** : https://www.linkedin.com/in/sourav-debnath-b4a80a313/
