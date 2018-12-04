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

def p_set_title(p):
    '''settitle : TITLE COLON STRING ENDLINE'''
    p[0] = p[3]

def p_set_events(p):
    '''setevent : EVENTS COLON STRING ENDLINE'''
    p[0] = p[3]

def p_set_location(p):
    '''setlocation : LOCATION COLON STRING ENDLINE'''
    p[0] = p[3]

def p_set_sendto(p):
    '''setsendto : SENDTO COLON STRING ENDLINE'''
    p[0] = p[3]

def p_create_event(p):
  '''expression : IDENTIFIER DOT NEW LBrace settitle setevent setlocation setsendto RBrace ENDLINE'''
  settings = {
      'Title': p[5],
      'Event': p[6],
      'Location': p[7],
      'SendTo': p[8]
  }
  createUI.setSettings(settings)

def p_initUI(p):
    '''expression : IDENTIFIER DOT INITUI LParen RParen'''
    createUI.start_ui()

def p_initDB(p):
    '''expression : IDENTIFIER DOT INITDB LParen RParen'''
    createUI.init_DB()


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
# s = 'UI.NEW{ Title : "Events"; Events : "fire"; Location : "Stefani";	SendTo : "All";};'
#s = 'UI.NEW{Title:"Catastrophe";Events:"fire";Location:"Stefani";SendTo:"All";};'

s = 'TITLE: "fire house";'

print("Input",s)
result = parser.parse(s)
print(result)
