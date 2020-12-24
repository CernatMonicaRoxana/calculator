from tokens import *
from calculator import expression

whitespaces = " \n\t"
digits = "0123456789"

expression = expression()
current_char = ""
position = -1


def advance():
    global expression, position, current_char
    position += 1
    if position < len(expression):
        current_char = expression[position]
    else:
        current_char = None


def generate_tokens():
    global position, whitespaces, digits, current_char
    while current_char is not None:
        if current_char in whitespaces:
            advance()
        elif current_char in digits or current_char == ".":
            yield generate_number()


def generate_number():
    global current_char
    dec_points = 0
    num = ""

    while current_char is not None and (current_char == '.' or current_char in digits):
        if current_char == ".":
            dec_points += 1
            if dec_points > 1:
                raise Exception("Not a legal float number, there is more than 1 decimal point in number\n")
        num += current_char
        advance()

    if dec_points == 0:
        return Token(TokenType.int_num, int(num))
    else:
        return Token(TokenType.float_num, float(num))


def main():
    tokens = generate_tokens()
    print(list(tokens))

main()