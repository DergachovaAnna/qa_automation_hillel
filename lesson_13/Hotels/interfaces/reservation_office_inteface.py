from abc import ABC, abstractmethod

class IReservationOffice(ABC):

    @abstractmethod
    def accept_reservation(self, number_of_rooms, name): ...
