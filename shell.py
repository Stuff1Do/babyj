import lexer
from sys import *
from tokentype import *

while True:
    text = input('babyj> ')
    if text.strip().lower() in ('byebye', 'exit', 'quit'):
        print("ByeBye!")
        break
    
    result,error = lexer.run(text)
    if error: print(error.as_string())
    else:
        for token in result:
            print(token)