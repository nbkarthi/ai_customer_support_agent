from strands import tool


@tool
def get_population(country: str) -> str:
    """Get the population of a country"""
    return f"The population of {country} is unknown"
