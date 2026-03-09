import asyncio
from strands import Agent
from models import model

def callback(**event):
    print(event)



agent = Agent(model=model, callback_handler=callback)

agent("What is AWS Lambda? keep it short and concise")
# async def main():
    
#     await agent("What is AWS Lambda? keep it short and concise")

# asyncio.run(main())