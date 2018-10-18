from ply.lex import *
reserved = []
tokens = ['IDENTIFIER', 'NUMBER', 'CHAR', 'DECLARATION', 'METHOD', 'EQUAL', 'ENDLINE'] + reserved


digit = r'[0-9]'
number = r'[0 | 1-9][0-9]*'
character = r'[a-zA-Z]'
lefparen = r'('
rigparen = r')'
identifier = r'' + character + r'(' + character + r'|' + number + r')*'
declaration = r'' + identifier + r'= (' + number + r'|' + character + r')* ;'
method = identifier + r'[(]' + r'[)]'

t_EQUAL = r'='
t_ENDLINE = r';'


# @TOKEN(declaration)
# def t_DECLARATION(t):
#     return t


# @TOKEN(method)
# def t_METHOD(t):
#     return t


@TOKEN(identifier)
def t_IDENTIFIER(t):
    return t


@TOKEN(number)
def t_NUMBER(t):
    t.value = int(t.value)
    return t


@TOKEN(character)
def t_CHAR(t):
    return t


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex(debug=0)
lexer.input('12')
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
