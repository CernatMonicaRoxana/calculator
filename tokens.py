from enum import Enum


class TokenType(Enum):
    Num = 0
    Add = 1
    Subtract = 2
    Multiply = 3
    L_P = 4
    R_P = 5
    Pow = 6
    Divide = 7
    Rad = 8
    Ln = 9
    Log = 10
    Sin = 11


class Token:
    def __init__(self, tip, value=None):
        self.type = tip
        self.value = value

    def __repr__(self):
        return self.type.name + (": {}".format(self.value) if self.value is not None else "")
