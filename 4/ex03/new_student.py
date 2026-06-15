import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """ Generates random id with 15 characters """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """ Dataclass representing a student with auto-generated login and ID """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False)

    def __post_init__(self):
        """ Initialize derived fields (login and id) after initialization """
        self.login = (self.name[0] + self.surname).capitalize()
        self.id = generate_id()
