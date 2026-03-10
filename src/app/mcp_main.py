import tracing  # noqa: F401 - must be first to configure OTEL
from mcp import stdio_client, StdioServerParameters
from strands import Agent
from strands.tools.mcp import MCPClient
from models import model
import logging
import asyncio


logging.getLogger("strands").setLevel(logging.INFO)
# Sets the logging format and streams logs to stderr
logging.basicConfig(
format="%(levelname)s | %(name)s | %(message)s",
handlers=[logging.StreamHandler()]
)


# Create MCP client with stdio transport
mcp_client = MCPClient(lambda: stdio_client(
    StdioServerParameters(
        command="uvx",
        args=["awslabs.aws-documentation-mcp-server@latest"]
    )
))


# Pass MCP client directly to agent - lifecycle managed automatically
agent = Agent(model=model, tools=[mcp_client])

# print("***************** List of tools *****************    ", flush=True)
# for tool in mcp_client.list_tools_sync():
#    print(f"{tool.tool_spec['name']}: {tool.tool_spec['description']}")
    # print(tool.tool_spec['name'])
# print("***************** List of tools *****************", flush=True)

agent("What is AWS Lambda? keep it short and concise")
# print(agent.messages)   


print("\nStreaming call:")
async def process_streaming_response():
    agent_stream = agent.stream_async("What is the capital of France and what is 42+7?")
    async for event in agent_stream:
    # Track event loop lifecycle
        if event.get("init_event_loop", False):
            print("🔄 Event loop initialized")
        elif event.get("start_event_loop", False):
            print("▶ Event loop cycle starting")
        elif event.get("start", False):
            print("📝 New cycle started")
        elif "message" in event:
         print(f"📬 New message created: {event['message']['role']}")
        elif event.get("complete", False):
         print("✅ Cycle completed")
        elif event.get("force_stop", False):
            print(
        f"🛑 Event loop force-stopped: {event.get('force_stop_reason', 'unknown reason')}")

print("Running streaming call...")  
asyncio.run(process_streaming_response())
print("Streaming call completed")