from tokens import *

whitespaces = " \n\t"
digits = "0123456789"


class Lexer:
    def __init__(self, expr):
        self.expr = expr
        self.pos = -1
        self.current_char = None
        self.advance()

    def advance(self):
        self.pos += 1
        if self.pos < len(self.expr):
            self.current_char = self.expr[self.pos]
        else:
            self.current_char = None

    def generate_tokens(self):
        while self.current_char is not None:
            if self.current_char in whitespaces:
                self.advance()
            elif self.current_char in digits or self.current_char == ".":
                yield self.generate_number()
            elif self.current_char == "+":
                self.advance()
                yield Token(TokenType.Add)
            elif self.current_char == "-":
                self.advance()
                yield Token(TokenType.Subtract)
            elif self.current_char == "*":
                self.advance()
                yield Token(TokenType.Multiply)
            elif self.current_char == "(":
                self.advance()
                yield Token(TokenType.L_P)
            elif self.current_char == ")":
                self.advance()
                yield  Token(TokenType.R_P)
            else:
                raise Exception("Illegal character {}".format(self.current_char))

    def generate_number(self):
        dec_points = 0
        num = ""

        while self.current_char is not None and (self.current_char == '.' or self.current_char in digits):
            if self.current_char == ".":
                dec_points += 1
                if dec_points > 1:
                    raise Exception("Not a legal float number, there is more than 1 decimal point in number\n")
            num += self.current_char
            self.advance()

        if num.startswith("."):
            num = "0" + num
        if num.endswith("."):
            num = num + "0"

        if dec_points == 0:
            return Token(TokenType.Num, int(num))
        else:
            return Token(TokenType.Num, float(num))

#
# def main():
#     tokens = generate_tokens()
#     print(list(tokens))
#
# # main()
