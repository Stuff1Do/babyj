import lexer

while True:
    text = input('babyj> ')
    if text.strip().lower() in ('byebye', 'exit', 'quit'):
        print("ByeBye!")
        break
    result = lexer.run(text)
    for token in result:
        print(token)