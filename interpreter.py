from nodes import NumberNode, AddNode, SubtractNode
from values import Number


class Interpreter:
    def visit(self, node):
        name = f"visit_{type(node).__name__}"  # AddNode => visit_AddNode
        method = getattr(self, name)
        return method(node)

    def visit_NumberNode(self, node):
        return Number(node.value)

    def visit_AddNode(self, node):
        return Number(self.visit(node.node_a).value + self.visit(node.node_b).value)

    def visit_SubtractNode(self, node):
        return Number(self.visit(node.node_a).value - self.visit(node.node_b).value)

    def visit_PlusNode(self, node):
        return Number(self.visit(node.value))
