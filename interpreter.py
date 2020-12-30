from nodes import *
from values import Number
from math import sqrt, log, sin, cos


class Interpreter:
    def visit(self, node):
        name = str(type(node).__name__)  # AddNode => AddNode
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

    def DivideNode(self, node):
        try:
            return Number(self.visit(node.node_a).value / self.visit(node.node_b).value)
        except Exception as e:
            raise Exception(e)

    def RadNode(self, node):
        return Number(sqrt(self.visit(node.node).value))

    def LnNode(self, node):
        return Number(log(self.visit(node.node).value))

    def LogNode(self, node):
        return Number(log(self.visit(node.node).value, 10))

    def SinNode(self, node):
        return Number(sin(self.visit(node.node).value))

    def CosNode(self, node):
        return Number(cos(self.visit(node.node).value))

    def CtgNode(self, node):
        return Number(cos(self.visit(node.node).value) / sin(self.visit(node.node).value))

    def TgNode(self, node):
        return Number(sin(self.visit(node.node).value) / cos(self.visit(node.node).value))

