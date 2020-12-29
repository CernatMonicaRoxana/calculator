from lexer import Lexer
from parse import Parser
from interpreter import Interpreter

while True:
    expr = input("Enter an expression: \n")
    lexer = Lexer(expr)
    tokens = lexer.generate_tokens()
    parser = Parser(tokens)
    tree = parser.parse()
    if not tree: continue
    interpreter = Interpreter()
    value = interpreter.visit(tree)
    print(value)

    # print(tree)
