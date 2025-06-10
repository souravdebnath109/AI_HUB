import os
from langchain_community.document_loaders import PDFMinerLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings, ChatHuggingFace, HuggingFaceEndpoint
from langchain_community.vectorstores import FAISS
from langchain.prompts import PromptTemplate

# Set HF API key
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_key"

# Prompt
prompt_template = PromptTemplate(
    template="Answer the question based on the following context:\n\n{context}\n\nQuestion: {question}\nAnswer:",
    input_variables=["context", "question"]
)

def analyze_pdf(query: str, pdf_path: str):
    try:
        loader = PDFMinerLoader(pdf_path)
        documents = loader.load()

        # Split text
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        docs = text_splitter.split_documents(documents)

        # Vector store
        embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
        vectorstore = FAISS.from_documents(docs, embeddings)
        retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

        # Get relevant context
        retrieved_docs = retriever.invoke(query)
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        # LLM
        llm = HuggingFaceEndpoint(
            repo_id="HuggingFaceH4/zephyr-7b-beta",
            task="text-generation",
            temperature=0.7,
            max_new_tokens=256
        )
        chat = ChatHuggingFace(llm=llm)

        # Run prompt
        formatted_prompt = prompt_template.format(context=context, question=query)
        response = chat.invoke(formatted_prompt)

        return {
            "pdf": os.path.basename(pdf_path),
            "answer": getattr(response, "content", str(response))
        }
    except Exception as e:
        return {"error": str(e)}
