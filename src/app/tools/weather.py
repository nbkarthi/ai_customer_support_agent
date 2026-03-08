from strands import tool

@tool
def get_weather(city: str) -> str:
    """Get the weather report for a city"""
    return f"The weather in {city} is sunny"
