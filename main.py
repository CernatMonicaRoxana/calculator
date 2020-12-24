from lexer import generate_tokens
from parse import Parser

tokens = list(generate_tokens())
parser = Parser(tokens)
tree = parser.parse()



