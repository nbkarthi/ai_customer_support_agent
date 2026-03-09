from strands import tool
from .booking_store import booking_store
from embedding import  search


## create_booking, delete_booking, get_booking
@tool
def create_booking(booking: dict) -> str:
    """Create a booking"""
    print(f"Creating booking: {booking}")
    return booking_store.create_booking(booking)

@tool
def delete_booking(booking_id: str) -> str:
    """Delete a booking"""
    print(f"Deleting booking: {booking_id}")
    return booking_store.delete_booking(booking_id)

@tool
def get_booking(booking_id: str) -> str:
    """Get a booking"""
    print(f"Getting booking: {booking_id}")
    return booking_store.get_booking(booking_id)

@tool
def search_restaurants(query: str) -> str:
    """Search for restaurants"""
    print(f"Searching for restaurants: {query}")
    return search(query)