from lexer import Lexer
from parse import Parser
from interpreter import Interpreter

print("""
                        Available functions:
    +, -, *, / , ^, log (base 10), ln (base e), rad, sin, cos, tg, ctg
    """)
while True:
    try:
        expr = input("Enter an expression: \n")
        lexer = Lexer(expr)
        tokens = lexer.generate_tokens()
        parser = Parser(tokens)
        tree = parser.parse()
        if not tree:
            continue
        interpreter = Interpreter()
        value = interpreter.visit(tree)
        print(value)

    except Exception as e:
        print(e)
