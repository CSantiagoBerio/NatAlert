from ply.yacc import *
from natlex import tokens

# import Tools
from UI import createUI

names = {}

def p_create_expression(p):
    '''create : DB DOT INIT LParen RParen ENDLINE UI DOT NEW LBrace TITLE COLON STRING ENDLINE EVENTS COLON string_list ENDLINE LOCATION COLON string_list ENDLINE SENDTO COLON string_list ENDLINE RBrace ENDLINE UI DOT INIT LParen RParen ENDLINE'''
    # print("Parsing DONE")
    createUI.init_db()
    settings = {
        'Title': p[13],
        'Event': ','.join(p[17]),
        'Location': ','.join(p[21]),
        'SendTo': ','.join(p[25])
    }
    createUI.set_settings(settings)
    createUI.start_ui()

def p_string_list(p):
    '''string_list : STRING COMMA string_list
                 | STRING'''
    if not isinstance(p[0], list):
        p[0] = list()
    p[0].append(p[1])
    if len(p) == 4:
        p[0] += p[3]


def p_error(p):
    print("Syntax error at: '%s'" % p.value)


parser = yacc()

print("Testing Parser. It should open a gui.")

file = open("input.txt", "r")
string = file.read()
result = parser.parse(string)
