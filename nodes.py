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


@dataclass
class PlusNode:
    node: any

    def __repr__(self):
        return "(+ {})".format(self.node)


@dataclass
class MinusNode:
    node: any

    def __repr__(self):
        return "(- {})".format(self.node)


@dataclass
class MultiplyNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return "({} * {})".format(self.node_a, self.node_b)


@dataclass
class PowNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return "({} ^ {})".format(self.node_a, self.node_b)


@dataclass
class DivideNode:
    node_a: any
    node_b: any

    def __repr__(self):
        return "({} / {})".format(self.node_a, self.node_b)


@dataclass
class RadNode:
    node: any

    def __repr__(self):
        return "(rad({}))".format(self.node)


@dataclass
class LnNode:
    node: any

    def __repr__(self):
        return "(ln({}))".format(self.node)


@dataclass
class LogNode:
    node: any

    def __repr__(self):
        return "(log({}))".format(self.node)


@dataclass
class SinNode:
    node: any

    def __repr__(self):
        return "(sin({}))".format(self.node)


@dataclass
class CosNode:
    node: any

    def __repr__(self):
        return "(cos({}))".format(self.node)
