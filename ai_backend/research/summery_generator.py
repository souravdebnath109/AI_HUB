from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate

# Set up the Gemini model
model = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key="gemini_api_key"  # 🔑 Replace with your actual API key
)

# Prompt template
prompt_template = PromptTemplate.from_template(
    "You are a research assistant. Your task is to summarize the following research topic in {style} style and {length} length:\n\n{topic}"
)

def generate_summary(topic: str, style: str, length: str) -> str:
    prompt = prompt_template.format(style=style, length=length, topic=topic)
    result = model.invoke(prompt)
    return getattr(result, "content", result)  # Some versions of LLMs return `content`, others return plain string
