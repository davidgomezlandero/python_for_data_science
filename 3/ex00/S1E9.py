from abc import ABC, abstractmethod


class Character(ABC):
    """ Base class for characters """
    def __init__(self, first_name, is_alive=True):
        """ Character constructor (first_name, is_alive=True) """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """ Set the character's is_alive status to False """
        pass


class Stark(Character):
    """ Stark character """
    def __init__(self, first_name, is_alive=True):
        """ Stark constructor (first_name, is_alive=True) """
        super().__init__(first_name, is_alive)

    def die(self):
        """ Set the character's is_alive status to False """
        self.is_alive = False
