from tokens import TokenType
from nodes import *


class Parser:
    def __init__(self, tokens):
        self.current_token = None
        self.tokens = iter(tokens)
        self.advance()

    def advance(self):
        try:
            self.current_token = next(self.tokens)
        except StopIteration:
            self.current_token = None

    def raise_error(self):
        raise Exception("Invalid syntax")

    def parse(self):
        if self.current_token is None:
            return None
        result = self.expr()

        if self.current_token is not None:
            self.raise_error()

        return result

    def expr(self):
        result = self.factor()
        while self.current_token is not None and self.current_token.type == TokenType.Add:
            if self.current_token.type == TokenType.Add:
                self.advance()
                result = AddNode(result, self.factor())

        return result

    def factor(self):
        token = self.current_token

        if token.type == TokenType.int_num or token.type == TokenType.float_num:
            self.advance()
            return NumberNode(token.value)

        self.raise_error()
