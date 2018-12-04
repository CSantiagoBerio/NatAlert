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


# def p_string_list(p):
#     '''string_list : STRING COMMA string_list
#                  | STRING'''
#     if not isinstance(p[0], list):
#         p[0] = list()
#     p[0].append(p[1])
#     if len(p) == 4:
#         p[0] += p[3]

def p_initUI(p):
    '''expression : UI DOT INIT LParen RParen'''
    createUI.start_ui()

def p_initDB(p):
    '''expression : DB DOT INIT LParen RParen'''
    createUI.init_db()

def p_create_event(p):
  '''expression : IDENTIFIER DOT NEW LBrace TITLE COLON STRING ENDLINE EVENTS COLON STRING ENDLINE LOCATION COLON STRING ENDLINE SENDTO COLON STRING ENDLINE RBrace ENDLINE'''
  #print("Parsing DONE")
  settings = {
      'Title': p[5],
      'Event': p[6],
      'Location': p[7],
      'SendTo': p[8]
  }
  createUI.set_settings(settings)

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
print("Testing Parser. It should open a gui.")
# s = '"yes","no"'
# s = 'UI.NEW{ TITLE : "Events"; Events : "fire"; Location : "Stefani";	SendTo : "All";};'
s = 'UI.NEW{TITLE:"Catastrophe";EVENTS:"fire";LOCATION:"Stefani";SENDTO:"All";};'
#s = 'UI.INIT()'

#s = 'TITLE: "Events";'
#s = 'LOCATION: "Fire";'
#s = 'LOCATION: "Stefani";'
#s = 'SENDTO: "ALL";'
#s = 'UI.INITDB()'
#s = 'SENDTO: "ALL";'

print("Input",s)
result = parser.parse(s)
print(result)
