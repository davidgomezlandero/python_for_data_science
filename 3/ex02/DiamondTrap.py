from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """ Inherits from both Baratheon and Lannister """
    def __init__(self, first_name, is_alive=True):
        """ King constructor """
        super().__init__(first_name, is_alive)
    
    @property
    def eyes(self):
        """ Get eye color """
        return self.__dict__['eyes']
    
    @eyes.setter
    def eyes(self, color):
        """ Set eye color """
        self.__dict__['eyes'] = color
    
    def get_eyes(self):
        """ Getter method for compatibility """
        return self.eyes
    
    def set_eyes(self, color):
        """ Setter method for compatibility """
        self.eyes = color

    @property
    def hairs(self):
        """ Get hairs color """
        return self.__dict__['hairs']
    
    @hairs.setter
    def hairs(self, color):
        """ Set hairs color """
        self.__dict__['hairs'] = color
    
    def get_hairs(self):
        """ Getter method for compatibility """
        return self.hairs
    
    def set_hairs(self, color):
        """ Setter method for compatibility """
        self.hairs = color
