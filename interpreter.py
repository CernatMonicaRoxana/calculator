from nodes import *
from values import Number
from math import pow

class Interpreter:
    def visit(self, node):
        name = f"{type(node).__name__}"  # AddNode => visit_AddNode
        method = getattr(self, name)
        return method(node)

    def NumberNode(self, node):
        return Number(node.value)

    def AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def PlusNode(self, node):
        return self.visit(node.node)

    def MinusNode(self, node):
        return Number(-self.visit(node.node).value)

    def MultiplyNode(self, node):
        return Number(self.visit(node.node_a).value * self.visit(node.node_b).value)

    def PowNode(self, node):
        return Number(self.visit(node.node_a).value ** self.visit(node.node_b).value)
