import os
import json


class BookingStore:
    def __init__(self):
        self.store = {}
        self.file_path = "bookings.json"

    def load(self):
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                self.store = json.load(f)

    def save(self):
        with open(self.file_path, "w") as f:
            json.dump(self.store, f)

    def create_booking(self, booking: dict) -> str:
        self.store[booking["id"]] = booking
        self.save()
        return f"Booking created: {booking}"

    def delete_booking(self, booking_id: str) -> str:
        self.store.pop(booking_id, None)
        self.save()
        return f"Booking deleted: {booking_id}"

    def get_booking(self, booking_id: str) -> str:
        return self.store.get(booking_id, None)


booking_store = BookingStore()
booking_store.load()
