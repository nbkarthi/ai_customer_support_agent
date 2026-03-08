from strands import Agent
from models import model
# from tools import create_booking, delete_booking, get_booking
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
# agent = Agent(model=model, tools=[create_booking, delete_booking, get_booking])

## Search the vector store for the top-k most similar documents
results = search("List italian restaurants in San Francisco", k=5)
print(results)
