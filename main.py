from lexer import generate_tokens


while True:
    lexer = generate_tokens()
    tokens = list(lexer)

    print(tokens)
