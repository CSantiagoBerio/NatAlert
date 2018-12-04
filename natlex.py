from ply.lex import *

#List of reserved words
reserved = {'if':'IF' ,
            'then':'THEN',
            'else':'ELSE',
            'while':'WHILE',
            'for':'FOR',
            'create':'CREATE',
            'let' : 'LET',
            'set' : 'SET',
            'get' : 'GET',
            'notify' : 'NOTIFY',
            'type' : 'TYPE',
            'comment' : 'COMMENT',
            'INIT' : 'INIT',
            'UI' : 'UI',
            'DB' : 'DB',
            'NEW' : 'NEW',
            'TITLE' : 'TITLE',
            'EVENTS' : 'EVENTS',
            'LOCATION' : 'LOCATION',
            'SENDTO' : 'SENDTO'}

#List of token names
tokens = ['STRING','IDENTIFIER', 'NUMBER', 'DOUBLE', 'CHAR', 'DECLARATION', 'METHOD', 'ASSIGN', 'ENDLINE','COMMA', 'DOT',
          'COLON', 'LParen', 'RParen', 'LBrace', 'RBrace'] + list(reserved.values())

#literals = "+-/*}{[]()"              #This are literal characters the lexer interprets them as they are

t_ignore = ' \t\n' #Ignored characters

#Regular Expression rules for simple tokens
digit = r'[0-9]'
number = r'[0 | 1-9][0-9]*'
character = r'[a-zA-Z]'
double = r'[-+]?[0-9]+(\.([0-9]+)?([eE][-+]?[0-9]+)?|[eE][-+]?[0-9]+)'
string = r'"([^"\n]|(\\"))*"'
#lefparen = r'('
#rigparen = r')'
identifier = r'' + character + r'(' + character + r'|' + number + r')*'
declaration = r'' + identifier + r'= (' + number + r'|' + character + r')* ;'
method = identifier + r'[(]' + r'[)]'



#Rule for new lines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


reserved_words_map = { }
for r in reserved:
    reserved_words_map[r.lower()] = r


@TOKEN(string)
def t_STRING(t):
    t.type = reserved.get(t.value, 'STRING')
    return t

@TOKEN(identifier)
def t_IDENTIFIER(t):
    t.type = reserved.get(t.value,'IDENTIFIER')              #This checks if the identifier is part of the reserved words
    return t

@TOKEN(declaration)
def t_DECLARATION(t):
    t.type = reserved.get(t.value,'DECLARATION')
    return t

@TOKEN(method)
def t_METHOD(t):
    return t

@TOKEN(double)
def t_DOUBLE(t):
    r'\d'
    return t

@TOKEN(number)
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

@TOKEN(character)
def t_CHAR(t):
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

t_ASSIGN = r'='
t_ENDLINE = r';'
t_COMMA = r','
# t_QUOTE = r'"'
t_COLON = r':'
t_DOT = r'.'
t_LParen = r'\('
t_RParen = r'\)'
t_LBrace = r'\{'
t_RBrace = r'\}'

#Literals

# def t_lbrace(t):
#     r'\{'
#     t.type='{'
#     return t
# def t_rbrace(t):
#     r'\}'
#     t.type = '}'
#     return t
# def t_lparen(t):
#     r'\('
#     t.type = '('
#     return t
# def t_rparen(t):
#     r'\)'
#     t.type = ')'
#     return t

def t_lbox(t):
    r'\['
    t.type = '['
    return t
def t_rbox(t):
    r'\]'
    t.type = ']'
    return t
def t_mult(t):
    r'\*'
    t.type = '*'
    return t
def t_res(t):
    r'\-'
    t.type = '-'
    return t
def t_sum(t):
    r'\+'
    t.type = '+'
    return t
def t_div(t):
    r'\/'
    t.type = '/'
    return t

def t_COMMENT(t):               #definition of a comment, it will not return anything when it reads a #___
    r'\#.*'
    pass

lexer = lex(debug=0)

print('Testing Lexer')
#lexer.input('1258403484934038585320029483905808203842028-185308-2-428-')
#lexer.input('x=12')
#lexer.input('hvhj')
#lexer.input('23.5423545')

#data = 'UI.NEW{ Title : "Events"; Events : "fire"; Location : "Stefani";	SendTo : "All";};'
#data = 'TITLE:"Events";'
file = open('input.txt', 'r')
data = file.read()

print("Input: ", data)
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break      # No more input
    print(tok)
