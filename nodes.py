from dataclasses import dataclass


@dataclass
class NumberNode:
    value: float

    def __repr__(self):
        return "{}".format(self.value)


@dataclass
class AddNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return "({} + {})".format(self.node_a, self.node_b)


@dataclass
class SubtractNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return "({} - {})".format(self.node_a, self.node_b)
