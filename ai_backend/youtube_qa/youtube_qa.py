
import uuid
import tempfile
import os

def run_youtube_qa(video_url: str, user_question: str) -> str:
    import yt_dlp
    import whisper
    from langchain.text_splitter import RecursiveCharacterTextSplitter
    from langchain_huggingface import HuggingFaceEmbeddings
    from langchain_community.vectorstores import FAISS
    from langchain_google_genai import GoogleGenerativeAI
    from langchain_core.prompts import PromptTemplate

    # Auth keys
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_key"
    os.environ["GOOGLE_API_KEY"] = "gemini_api_key"

    # Create a unique filename
    uid = str(uuid.uuid4())
    audio_filename = f"{uid}.mp3"

    # Download audio
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': f'{uid}.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': True,
        'no_warnings': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

    # Transcribe
    model = whisper.load_model("base")
    result = model.transcribe(audio_filename)
    transcript = result["text"]

    # Split + embed
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.create_documents([transcript])
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_store = FAISS.from_documents(chunks, embeddings)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    # Prompt + LLM
    llm = GoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.2)
    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""You are an expert summarizer. Based on the context below, answer the user's question accurately and concisely.\n\nContext:\n{context}\n\nQuestion:\n{question}\n\nAnswer:\n"""
    )
    retrieved_docs = retriever.invoke(user_question)
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    final_prompt = prompt.format(context=context_text, question=user_question)
    answer = llm.invoke(final_prompt)

    # Clean up audio file
    try:
        os.remove(audio_filename)
    except Exception:
        pass  # Ignore if file is already deleted

    return getattr(answer, "content", answer)
