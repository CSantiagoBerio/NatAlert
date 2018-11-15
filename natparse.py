from ply.yacc import *
from natlex import tokens

#import Tools
from UI.createUI import *

names = {}

def p_expression_number(p):
    '''expression : NUMBER'''
    p[0] = p[2]

def p_expression_string(p):
    '''expression : QUOTE expression QUOTE'''
    p[0] = p[2]

def p_create_event(p):
    '''expression : CREATE EVENT lefparen TYPE EQUAL expression COMMA LOCATION EQUAL expression COMMA
    SENDTO EQUAL expression'''

def p_declaration_expression(p):
    '''declaration : LET identifier EQUAL expression'''
    names[p[1]] = p[3]

def p_initUI(p):
    '''expression : INITUI lefparen expression rigparen'''
    global ui
    ui = UIClass.UIClass()
    ui.initUI()

def p_initDB(p):
    '''expression : INITDB lefparen expression rigparen'''
    ui.initDb()

#-------------------- Currently not in use ------------
# def p_declaration_event(p):
#     '''declaration : LET identifier EQUAL CREATE EVENT lefparen TYPE EQUAL expression COMMA LOCATION EQUAL expression COMMA
#     SENDTO EQUAL expression'''
#     names{p[0]} = p[2]
#
#
#
# def p_set(p):
#     '''expression : SET identifier DOT TYPE expression
#                   | SET identifier DOT LOCATION expression
#                   | SET identifier DOT SENDTO expression
#                   | SET identifier DOT COMMENT expression'''
#
#     if p[4] == 'TYPE':
#
#     elif p[4] == 'LOCATION':
#
#     elif p[4] == 'SENDTO':


# def p_get(p):
#     '''expression : GET identifier DOT TYPE
#                   | GET identifier DOT LOCATION
#                   | GET identifier DOT SENDTO'''
#
#     if p[4] == 'TYPE':
#
#     elif p[4] == 'LOCATION':
#
#     elif p[4] == 'SENDTO':
#
# def p_notify(p):
#     '''notify : NOTIFY lefparen identifier rigparen'''


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
s = 'initUI("5")'
result = parser.parse(s)
print(result)
