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

    def raise_error(self, token):
        raise Exception("Invalid syntax {}".format(token))

    def parse(self):
        if self.current_token is None:
            return None
        result = self.expr()

        if self.current_token is not None:
            self.raise_error(self.current_token)

        return result

    def expr(self):
        result = self.term()
        while self.current_token is not None and self.current_token.type in (TokenType.Add, TokenType.Subtract):
            if self.current_token.type == TokenType.Add:
                self.advance()
                result = AddNode(result, self.term())
            elif self.current_token.type == TokenType.Subtract:
                self.advance()
                result = SubtractNode(result, self.term())

        return result

    def term(self):
        result = self.base()
        while self.current_token is not None and self.current_token.type in (TokenType.Multiply, TokenType.Divide):
            if self.current_token.type == TokenType.Multiply:
                self.advance()
                result = MultiplyNode(result, self.base())
            elif self.current_token.type == TokenType.Divide:
                self.advance()
                result = DivideNode(result, self.base())

        return result

    def base(self):
        result = self.factor()
        while self.current_token is not None and self.current_token.type == TokenType.Pow:
            if self.current_token.type == TokenType.Pow:
                self.advance()
                result = PowNode(result, self.factor())
        return result

    # def rad(self):
    #     result = self.factor()
    #     while self.current_token is not None and self.current_token.type == TokenType.Rad:
    #         if self.current_token.type == TokenType.Rad:
    #
    #             self.advance()
    #
    #             if self.current_token.type != TokenType.L_P:
    #                 self.raise_error(self.current_token)
    #
    #             self.advance()
    #
    #             result = RadNode(self.expr())
    #
    #             self.advance()
    #
    #             if self.current_token.type != TokenType.R_P:
    #                 self.raise_error(self.current_token)
    #
    #             self.advance()
    #
    #         return result

    def factor(self):
        token = self.current_token

        if token.type == TokenType.Rad:
            self.advance()
            if self.current_token.type != TokenType.L_P:
                self.raise_error(self.current_token)

            self.advance()
            result = RadNode(self.expr())

            if self.current_token.type != TokenType.R_P:
                self.raise_error(self.current_token)

            self.advance()
            return result

        if token.type == TokenType.Ln:
            self.advance()
            if self.current_token.type != TokenType.L_P:
                self.raise_error(self.current_token)

            self.advance()
            result = LnNode(self.expr())

            if self.current_token.type != TokenType.R_P:
                self.raise_error(self.current_token)

            self.advance()
            return result

        if token.type == TokenType.Log:
            self.advance()
            if self.current_token.type != TokenType.L_P:
                self.raise_error(self.current_token)

            self.advance()
            result = LogNode(self.expr())

            if self.current_token.type != TokenType.R_P:
                self.raise_error(self.current_token)

            self.advance()
            return result

        if token.type == TokenType.Sin:
            self.advance()
            if self.current_token.type != TokenType.L_P:
                self.raise_error(self.current_token)

            self.advance()
            result = SinNode(self.expr())

            if self.current_token.type != TokenType.R_P:
                self.raise_error(self.current_token)

            self.advance()
            return result

        if token.type == TokenType.Cos:
            self.advance()
            if self.current_token.type != TokenType.L_P:
                self.raise_error(self.current_token)

            self.advance()
            result = CosNode(self.expr())

            if self.current_token.type != TokenType.R_P:
                self.raise_error(self.current_token)

            self.advance()
            return result

        if token.type == TokenType.Ctg:
            self.advance()
            if self.current_token.type != TokenType.L_P:
                self.raise_error(self.current_token)

            self.advance()
            result = CtgNode(self.expr())

            if self.current_token.type != TokenType.R_P:
                self.raise_error(self.current_token)

            self.advance()
            return result

        if token.type == TokenType.L_P:
            self.advance()
            result = self.expr()

            if self.current_token.type != TokenType.R_P:
                self.raise_error(self.current_token)

            self.advance()

            return result

        if token.type == TokenType.Num:
            self.advance()
            return NumberNode(token.value)

        elif token.type == TokenType.Add:
            self.advance()
            return PlusNode(self.factor())

        elif token.type == TokenType.Subtract:
            self.advance()
            return MinusNode(self.factor())

        self.raise_error(self.current_token)

