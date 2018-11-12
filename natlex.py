#from ply import lex
#import ply.yacc as yacc
from ply.lex import *

reserved = {'if':'IF' ,'then':'THEN','then':'THEN','else':'ELSE','while':'WHILE','for':'FOR','catastrophe':'CATASTROPHE'}
tokens = ['IDENTIFIER', 'NUMBER', 'CHAR', 'DECLARATION', 'METHOD', 'EQUAL', 'ENDLINE'] + reserved.values()

digit = r'[0-9]'
number = r'[0 | 1-9][0-9]*'
character = r'[a-zA-Z]'
lefparen = r'('
rigparen = r')'
identifier = r'' + character + r'(' + character + r'|' + number + r')*'
declaration = r'' + identifier + r'= (' + number + r'|' + character + r')* ;'
method = identifier + r'[(]' + r'[)]'
#catastrophe = r'[hurricane]'+character
#category = r'[1-5]'
#coordinates = r'' + lefparen + number + r'.'+number+r','+number+'.'+number+rigparen
t_EQUAL = r'='
t_ENDLINE = r';'

@TOKEN(identifier)
def t_IDENTIFIER(t):
    t.type = reserved.values(t.value,'IDENTIFIER') #This checks if the identifier is part of the reserved words
    return t


@TOKEN(number)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


@TOKEN(character)
def t_CHAR(t):
    return t

@TOKEN(declaration)
def t_DECLARATION(t):
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

#Aparece en el tutorial
def t_newLine(t):
    r' \n+'
    t.lexer.lineno+=len(t.value)

def t_COMMENT(t):               #definition of a comment, it will not return anything when it reads a #___
    r'\#.*'
    pass

lexer = lex(debug=0)

lexer.input('12584034849340385853200294839058082038420280488350647352081-185308-2-428-')
lexer.input('x=12')

#data = '3 + 4 * 10+ -20 *2'
#lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
