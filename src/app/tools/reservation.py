from strands import tool
from src.app.tools.booking_store import booking_store



## create_booking, delete_booking, get_booking
@tool
def create_booking(booking: dict) -> str:
    """Create a booking"""
    return booking_store.create_booking(booking)

@tool
def delete_booking(booking_id: str) -> str:
    """Delete a booking"""
    return booking_store.delete_booking(booking_id)

@tool
def get_booking(booking_id: str) -> str:
    """Get a booking"""
    return booking_store.get_booking(booking_id)
    