from strands import Agent
from models import model
from tools import create_booking, delete_booking, get_booking, search_restaurants
import logging
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
from embedding import load_vectorstore, search


logging.getLogger("strands").setLevel(logging.INFO)
# Sets the logging format and streams logs to stderr
logging.basicConfig(
format="%(levelname)s | %(name)s | %(message)s",
handlers=[logging.StreamHandler()]
)


## Initialize the agent
agent = Agent(model=model, tools=[create_booking, delete_booking, get_booking, search_restaurants])


## Call the agent and pass the RAG results as context
agent("List italian restaurants in San Francisco")

agent("Create a booking for Casa Mexicana in San Francisco on 10/03/2026 at 18:00 for 2 people with id as 1")
result = agent("Get bookings with id 1")
# agent("Delete the booking with id 1")
# agent("Get the booking with id 1")
print(agent.messages)
print(result.metrics)
