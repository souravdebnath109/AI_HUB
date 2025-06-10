from langchain_core.tools import tool
from langchain_google_genai import GoogleGenerativeAI
from langchain.agents import initialize_agent, AgentType
import requests

# === API Credentials ===
EXCHANGE_API_KEY = "exchange_api_key"
BASE_URL = "http://api.exchangeratesapi.io/v1/latest"

# === Tool 1: Get Conversion Rate from EUR to any supported currency ===
@tool
def get_eur_to_currency(currency: str) -> float:
    """
    Get the conversion rate from EUR to the given currency.
    """
    url = f"{BASE_URL}?access_key={EXCHANGE_API_KEY}&symbols={currency}"
    response = requests.get(url)
    data = response.json()

    if "rates" not in data or currency not in data["rates"]:
        raise ValueError(f"Could not get conversion rate for {currency}. Response: {data}")
    
    return data["rates"][currency]

# === Tool 2: Convert Currency ===
@tool
def convert(value: float, rate: float) -> float:
    """
    Convert value using conversion rate.
    """
    return value * rate

# ✅ Tool 3: Calculate Rate
@tool
def calculate_rate(rate_from: float, rate_to: float) -> float:
    """
    Compute conversion rate from two EUR-based rates.
    Returns: rate_to / rate_from
    """
    return rate_to / rate_from

# === Gemini LLM Setup ===
llm = GoogleGenerativeAI(
    model="gemini-2.0-flash-lite",
    api_key="gemini_api_key",
    temperature=0
)

# === Agent Setup ===
agent_executor = initialize_agent(
    tools=[get_eur_to_currency, convert, calculate_rate],
    llm=llm,
    agent=AgentType.STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True,
    handle_parsing_errors=True,
)

# === Reusable Function for Django or CLI ===
def run_conversion_agent(amount: float, from_currency: str, to_currency: str) -> float:
    instruction = f"""
Step-by-step:
1. Use get_eur_to_currency('{from_currency}') → eur_from
2. Use get_eur_to_currency('{to_currency}') → eur_to
3. Use calculate_rate(rate_from=eur_from, rate_to=eur_to) → final_rate
4. Use convert(value={amount}, rate=final_rate)
Only return the final numeric result (no explanation).
"""
    question = f"What is {amount} {from_currency} in {to_currency}?"
    result = agent_executor.invoke({"input": instruction + question})

    output = result.get("output", "")
    try:
        value = float("".join(ch for ch in output if (ch.isdigit() or ch == ".")))
        return round(value, 4)
    except:
        raise ValueError(f"agent response: {output}")
