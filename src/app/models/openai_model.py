from strands.models.openai import OpenAIModel
from strands.models.ollama import OllamaModel
from dotenv import load_dotenv
import os

load_dotenv()

model = OpenAIModel(
    client_args={"api_key": os.getenv("OPENAI_API_KEY")},
    model_id="gpt-4o-mini",
)

## Connect to OOlama model Qwen2.5-72b-instruct
# model = OllamaModel(
#     model_id="qwen2.5:7b-instruct",
#     host="http://localhost:11434",
# )