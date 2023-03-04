from abc import ABC, abstractmethod


class IReception(ABC):

    @abstractmethod
    def confirm_capacity(self): ...

    @abstractmethod
    def check_in(self, number_of_rooms): ...

    @abstractmethod
    def check_out(self, number_of_rooms): ...
