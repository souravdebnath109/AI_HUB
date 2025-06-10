# weather/agent.py

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.tools import tool
import requests
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate

# === Tool: DuckDuckGo Search ===
search_tool = DuckDuckGoSearchRun()

# === Tool: Get Weather Data ===
@tool
def get_weather_data(location: str) -> str:
    """
    Fetches the current weather for a given location using OpenWeatherMap API.
    """
    geo_resp = requests.get("https://nominatim.openstreetmap.org/search", params={
        "q": location,
        "format": "json"
    })
    if geo_resp.status_code != 200 or not geo_resp.json():
        return f"Could not find coordinates for '{location}'."
    
    lat = geo_resp.json()[0]["lat"]
    lon = geo_resp.json()[0]["lon"]

    api_key = "weather_api_key"  # Replace with actual API key
    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    weather_resp = requests.get(weather_url, params={
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric",
        "lang": "en"
    })

    if weather_resp.status_code != 200:
        return f"Error fetching weather data: {weather_resp.text}"

    data = weather_resp.json()
    weather = data['weather'][0]['description']
    temp = data['main']['temp']
    city_name = data.get('name', location)

    return f"The current weather in {city_name} is {weather} with a temperature of {temp}°C."

# === LLM + Prompt Setup ===
llm = GoogleGenerativeAI(
    model="gemini-1.5-flash",
    api_key="gemini_api_key",  # 🔁 Replace with actual key
    temperature=0
)

prompt_template = PromptTemplate.from_template("""
Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
{agent_scratchpad}
""")

tools = [search_tool, get_weather_data]

agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt_template
)

agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True
)

# === Function to Call Agent ===
def get_weather_response(user_input: str) -> str:
    result = agent_executor.invoke({"input": user_input})
    return result.get("output", "No output returned.")
