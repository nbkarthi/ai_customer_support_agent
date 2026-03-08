from strands import Agent,tool
from strands.models.openai import OpenAIModel
from dotenv import load_dotenv
import os

## Init OS Environment Variables
load_dotenv()

## Initialize the OpenAI model provider
model = OpenAIModel(
    client_args={"api_key": os.getenv("OPENAI_API_KEY")},
    model_id="gpt-4o-mini",
)

## define a tool to get a weather report
@tool
def get_weather(city: str) -> str:
    """Get the weather report for a city"""
    return f"The weather in {city} is sunny"

## define a tool to get capital of a country
@tool
def get_capital(country: str) -> str:
    """Get the capital of a country"""
    return f"The capital of {country} is {country.capitalize()}"

## define a tool to get the population of a country
@tool
def get_population(country: str) -> str:
    """Get the population of a country"""
    return f"The population of {country} is {country.population}"

## Initialize the agent
agent = Agent(model=model, tools=[get_weather, get_capital, get_population])

## Call the agent
weather_result = agent("What is the weather of France?")
print(weather_result.message)

capital_result = agent("What is the capital of France?")
print(capital_result.message)

population_result = agent("What is the population of France?")
print(population_result.message)
