from enum import Enum


class TokenType(Enum):
    int_num = 0
    float_num = 1
    Add = 2


class Token:
    def __init__(self, tip, value=None):
        self.type = tip
        self.value = value

    def __repr__(self):
        return self.type.name + (": {}".format(self.value) if self.value is not None else "")
