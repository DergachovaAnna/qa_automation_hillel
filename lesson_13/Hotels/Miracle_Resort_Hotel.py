from lesson_13.Hotels.interfaces.housekeepeng_interface import IHousekeeping
from lesson_13.Hotels.interfaces.reception_interface import IReception
from lesson_13.Hotels.interfaces.reservation_office_inteface import IReservationOffice
import random
from datetime import datetime


# Inheritance, Abstraction
class MiracleHotel(IHousekeeping, IReception, IReservationOffice):
    # hiding
    __rooms_status = {1: "Free", 2: "Free", 3: "Free", 4: "Free",
                      5: "Free", 6: "Free", 7: "Free", 8: "Free",
                      9: "Free", 10: "Free", 11: "Free", 12: "Free",
                      13: "Free", 14: "Free", 15: "Free", 16: "Free",
                      17: "Free", 18: "Free", 19: "Free", 20: "Free"}

    def __init__(self):
        self.capacity = 20
        self.current_capacity = 0
        self.free_rooms = None
        self.overbooking = False
        self.cleaning_required = False

    # incapsulation
    @property
    def get_rooms_status(self):
        return self.__rooms_status

    # polimorfizm, incapsulation
    def accept_reservation(self, number_of_rooms: int, name: str):
        """
        Accept a reservation with a given number of rooms and name,
        as long as there are enough free rooms or the hotel can overbook

        Parameters:
                number_of_rooms (int): the number of rooms requested in the reservation
                name (str): the name of the person making the reservation

        Returns: a message indicating whether the reservation was accepted or not
        """
        overbooking_possibility = 5  # max number of rooms, that
        # Reservation office may accept reservation for, even if they are taken right now
        self.free_rooms = self.capacity - self.current_capacity
        if self.free_rooms >= number_of_rooms > 0:
            return f'Reservation made on name "{name}" is accepted.'
        elif number_of_rooms <= 0:
            return 'Reservation for negative rooms value cant be made.'
        elif self.free_rooms < number_of_rooms and number_of_rooms - self.free_rooms <= overbooking_possibility:
            self.overbooking = True
            overbooking_possibility -= 1
            return f'Reservation made on name {name} is accepted.'
        else:
            return f'We apologise, but reservation can not be accepted - the hotel is fully booked'

    # polimorfizm, incapsulation
    def confirm_capacity(self):
        """
        Confirms current capacity of the hotel, taking overbooking into account
        Returns: message indicating the current capacity of the hotel
        """
        if self.overbooking:
            return f'Current capacity: {self.current_capacity} rooms (excluding overbookings)'
        else:
            return f'Current capacity: {self.current_capacity} rooms'

    # polimorfizm, incapsulation
    def check_in(self, number_of_rooms: int):
        """
        Check in to a given number of rooms, selecting random available rooms from the hotel.
        Parameters - number_of_rooms (int) - the number of rooms to check in to
        Returns: message indicating which rooms were checked in to or were not checked in
        """
        occupied_rooms = []
        if number_of_rooms > 0:
            for room in range(number_of_rooms):
                available_rooms = [room for room, status in self.__rooms_status.items() if status == 'Free']
                if available_rooms:
                    room_to_assign = random.choice(available_rooms)
                    self.__rooms_status[room_to_assign] = 'Occupied'
                    occupied_rooms.append(room_to_assign)
                    self.current_capacity += 1
                else:
                    break
        else:
            raise ValueError(f'number_of_rooms can not be zero or negative value!!!')

        if len(occupied_rooms) < number_of_rooms:
            return f'We gave you all available rooms, but no more free rooms left for tonight. ' \
                   f'Seems like we are overbooked..'

        if occupied_rooms:
            return f'Checked in to rooms {occupied_rooms}'
        else:
            return 'No available rooms to check in.'

    # polimorfizm, incapsulation
    def check_out(self, number_of_rooms):
        """
        Check out given number of rooms, selecting random  occuied rooms
        Parameters - number_of_rooms (int) - the number of rooms to check out
        Returns: message indicating that rooms were checked out
        """
        occupied_rooms = [room for room, status in self.__rooms_status.items() if status == 'Occupied']
        if len(occupied_rooms) < number_of_rooms:
            return f'Cant check out {number_of_rooms} rooms - only {len(occupied_rooms)} rooms is occupied.'
        if number_of_rooms < 0:
            raise ValueError(f'number_of_rooms can not be zero or negative value!!!')
        for room in range(number_of_rooms):
            room_to_vacate = random.choice(occupied_rooms)
            self.__rooms_status[room_to_vacate] = 'Free'
            occupied_rooms.remove(room_to_vacate)
            self.current_capacity -= 1
        self.cleaning_required = True
        return f'Checked out of {number_of_rooms} rooms.'

    # polimorfizm, incapsulation
    def refill_fridge(self):
        """
        Function represent HK service fork. Fridge should be refilled after room has been cleaned
        """
        if not self.cleaning_required:
            return "Fridge has been refilled."
        else:
            return "Fridge should be refilled after cleaning"

    # polimorfizm, incapsulation
    def report_to_reception(self, room_number: int):
        """
        Function represent HK service fork. HK check if room is free and cleaned and reports to reception,
        if it is available

        Returns: str: message indicating that room is ready or not
        """

        if self.__rooms_status[room_number] == "Free" and not self.cleaning_required:
            return f"Room {room_number} is ready for new guests."
        else:
            return f"Room {room_number} is not yet ready for new guests."

    # polimorfizm, incapsulation
    def clean_room(self):
        """
        Function represent HK service fork. HK will clean rooms at set hour
        if rooms became free and cleaning is required after previous guests checkout

        Returns: str: message indicating that the room cleaned or occupied and will not be cleaned yet
        """
        now = datetime.now()
        if now.hour == 22:
            for room_number, status in self.__rooms_status.items():
                if status == "Free":
                    self.cleaning_required = False
                    print(f"Room {room_number} has been cleaned")
            return "All occupied rooms will be cleaned after check out."
        else:
            return "It is not yet time to clean the rooms :)"


if __name__ == '__main__':
    hotel = MiracleHotel()
    print(hotel.confirm_capacity())
    print(hotel.report_to_reception(1))
    print(hotel.check_in(30))
    print(hotel.confirm_capacity())
    print(hotel.get_rooms_status)
    print(hotel.check_out(7))
    print(hotel.get_rooms_status)
    print(hotel.check_in(7))
    print(hotel.check_in(1))
    print(hotel.confirm_capacity())
    print(hotel.clean_room())
    print(hotel.check_out(7))
    print(hotel.get_rooms_status)
    print(hotel.clean_room())
    print(hotel.refill_fridge())
    print(hotel.check_in(1))
    print(hotel.check_out(1))
    print(hotel.refill_fridge())
    print(hotel.clean_room())
    print(hotel.refill_fridge())
    print(hotel.confirm_capacity())
    print(hotel.accept_reservation(19, 'Anna'))
    print(hotel.accept_reservation(12, 'Anna'))
    print(hotel.confirm_capacity())
