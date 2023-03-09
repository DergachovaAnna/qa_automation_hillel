from abc import ABC, abstractmethod


class IHousekeeping(ABC):

    @abstractmethod
    def clean_room(self): ...

    @abstractmethod
    def refill_fridge(self): ...

    @abstractmethod
    def report_to_reception(self, room_number): ...
