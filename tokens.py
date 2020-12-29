from enum import Enum


class TokenType(Enum):
    Num = 0
    Add = 1
    Subtract = 2
    Multiply = 3


class Token:
    def __init__(self, tip, value=None):
        self.type = tip
        self.value = value

    def __repr__(self):
        return self.type.name + (": {}".format(self.value) if self.value is not None else "")
