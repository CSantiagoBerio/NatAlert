from ply.yacc import *
from natlex import tokens


def p_declaration(p):
    '''declaration : IDENTIFIER EQUAL NUMBER ENDLINE'''


def p_error(p):
    print("Syntax error in input!")


parser = yacc()

# while True:
#     try:
#         s = 'chris12 = 0;'
#     except EOFError:
#         break
#     if not s:
#         continue
s = 'a = 0;'
result = parser.parse(s)
print(result)
