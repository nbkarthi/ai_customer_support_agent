from strands import tool


@tool
def get_capital(country: str) -> str:
    """Get the capital of a country"""
    return f"The capital of {country} is {country.capitalize()}"
