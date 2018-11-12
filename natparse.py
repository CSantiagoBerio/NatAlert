from ply.yacc import *
from natlex import tokens


def p_declaration(p):
    '''declaration : IDENTIFIER EQUAL NUMBER ENDLINE'''


def p_error(p):
    print("Syntax error in input!")
#HAy que a~adir estos como metodos de parser
##,'COORDINATES','CATASTROPHE', 'CATEGORY'
#CADA toquen tiene q tener su def expression

def p_category(p):
    ''''''
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
