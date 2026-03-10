import tracing  # noqa: F401 - must be first to configure OTEL
from strands import Agent
from models import model
from tools import get_weather, get_capital, get_population
import logging

logging.getLogger("strands").setLevel(logging.INFO)
# Sets the logging format and streams logs to stderr
logging.basicConfig(
format="%(levelname)s | %(name)s | %(message)s",
handlers=[logging.StreamHandler()]
)



## Initialize the agent
agent = Agent(model=model, tools=[get_weather, get_capital, get_population])

## Call the agents
weather_result = agent("What is the weather of France?")
print(weather_result.message)

# capital_result = agent("What is the capital of France?")
# print(capital_result.message)

# population_result = agent("What is the population of France?")
# print(population_result.message)
