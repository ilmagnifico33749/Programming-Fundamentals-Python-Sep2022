# from room import Room
from project.room import Room


class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = list()
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count: int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                if room.is_taken is False:
                    room.take_room(people)
                    self.guests += room.guests

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        return f"Hotel {self.name} has {self.guests} total guests\n" \
               f"Free rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken is False])}\n" \
               f"Taken rooms: {', '.join([str(room.number) for room in self.rooms if room.is_taken is True])}"
