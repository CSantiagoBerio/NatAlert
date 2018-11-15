from ply.yacc import *
from natlex import tokens

names = {}

def p_coordinate(p):
    '''coordinate : lefparen number comma number rigparen'''
    p[0] = (p[2],p[4])

def p_factor_expression(p):
    '''factor : expression'''
    p[0] = p[1]

def p_factor_number(p):
    '''factor : number'''
    p[0] = p[1]

def p_declaration(p):
    '''declaration : LET IDENTIFIER EQUAL expression'''
    names[p[0]] = p[4]

def p_expression_term(p):
    '''expression : term'''
    p[0] = p[1]

def p_expression_declaration(p):
    '''expression : declaration'''
    p[0] = p[1]

def p_expression_method(p):
    '''expression : method'''
    p[0] = p[1]

def p_expression_cond(p):
    '''expression : IF expression THEN expression ELSE expression'''
    if p[3]:
        p[0] = p[4]
    else:
        if p[6] is not None:
            p[0] = p[6]

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
