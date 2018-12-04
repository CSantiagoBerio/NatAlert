from ply.yacc import *
from natlex import tokens

#import Tools
from UI import createUI

names = {}

# def p_string_list(p):
#     '''string_list : STRING
#                  | string_list COMMA STRING'''
#     if len(p) == 2:
#        p[0] = [p[1]]
#     else:
#        p[0] = p[1] + [p[3]]

# def p_string(p):
#     '''
#     expression : STRING COMMA STRING
#     expression : STRING
#     '''
#     if len(p) == 2:
#         p[0] = [p[1]]
#     else:
#         p[0] = p[1]
#         p[0].append(p[3])

# def p_string(p):
#     '''string : STRING'''
#     p[0] = p[1]

# def p_init(p):
#     '''expression : UI DOT INIT LParen RParen ENDLINE
#                     | DB DOT INIT LParen RParen ENDLINE'''
#     if(p[1] == 'UI'):
#         createUI.start_ui()
#     elif(p[1] == 'DB'):
#         createUI.init_db()

def p_create_expression(p):
    '''expression : UI DOT NEW LBrace TITLE COLON STRING ENDLINE EVENTS COLON string_list ENDLINE LOCATION COLON string_list ENDLINE SENDTO COLON string_list ENDLINE RBrace ENDLINE'''
    # print("Parsing DONE")
    settings = {
        'Title': p[7],
        'Event': ",".join(p[11]),
        'Location': ",".join(p[15]),
        'SendTo': ",".join(p[19])
    }
    createUI.set_settings(settings)

def p_string_list(p):
    '''string_list : STRING COMMA string_list
                 | STRING'''
    if not isinstance(p[0], list):
        p[0] = list()
    p[0].append(p[1])
    if len(p) == 4:
        p[0] += p[3]

def p_initDB_expression(p):
    '''expression : DB DOT INIT LParen RParen ENDLINE'''
    createUI.init_db()

def p_initUI_expression(p):
    '''expression : UI DOT INIT LParen RParen ENDLINE'''
    createUI.start_ui()

def p_error(p):
    print("Syntax error at: '%s'" % p.value)

parser = yacc()


# while True:
#     try:
#         s = 'chris12 = 0;'
#     except EOFError:
#         break
#     if not s:
#         continue
print("Testing Parser. It should open a gui.")
# s = '"yes","no"'
# s = 'UI.NEW{ TITLE : "Events"; Events : "fire"; Location : "Stefani";	SendTo : "All";};'
#s = 'UI.NEW{TITLE:"Catastrophe";EVENTS:"fire";LOCATION:"Stefani";SENDTO:"All";};'
#s = 'UI.INIT()'
#s = '"new", "data"'
#s = '"new"'

#s = 'TITLE: "Events";'
#s = 'LOCATION: "Fire";'
#s = 'LOCATION: "Stefani";'
#s = 'SENDTO: "ALL";'
#s = 'UI.INITDB()'
#s = 'SENDTO: "ALL";'

file = open("input.txt", "r")
string = file.read()

print("Input",string)
result = parser.parse(string)
print(result)
