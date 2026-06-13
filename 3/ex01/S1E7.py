from S1E9 import Character


class Baratheon(Character):
    """ Baratheon character class"""
    def __init__(self, first_name, is_alive=True):
        """ Baratheon constructor """
        super().__init__(first_name, is_alive)
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """ Set the character's is_alive status to False """
        self.is_alive = False

    def __str__(self):
        """ What print()/str() displays """
        return (f"Vector: ('{self.family_name}', \
'{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """ Official representation, repr() """
        return (f"Vector: ('{self.family_name}', \
'{self.eyes}', '{self.hairs}')")


class Lannister(Character):
    """ Lannister character class"""
    def __init__(self, first_name, is_alive=True):
        """ Lannister constructor """
        super().__init__(first_name, is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """ Set the character's is_alive status to False """
        self.is_alive = False

    def __str__(self):
        """ What print()/str() displays """
        return (f"Vector: ('{self.family_name}', \
'{self.eyes}', '{self.hairs}')")

    def __repr__(self):
        """ Official representation, repr() """
        return (f"Vector: ('{self.family_name}', \
'{self.eyes}', '{self.hairs}')")

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """ Factory method - creates and returns an instance """
        return cls(first_name, is_alive)
