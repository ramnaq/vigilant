import ply.lex as lex
import ply.yacc as yacc


# Create reserved words
reserved = {
    'if': 'IF',
    'then': 'THEN',
    'else': 'ELSE',
    'for': 'FOR',
    'break': 'BREAK',
    'print': 'PRINT',
    'return': 'RETURN',
    'def': 'DEF',
    'new': 'NEW',
    'null': 'NULL',
    'read': 'READ'
}

# Create tokens
tokens = [
    'FLOAT',
    'FLOAT_CONSTANT',
    'INT',
    'INT_CONSTANT',
    'IDENT',
    'STRING',
    'STRING_CONSTANT',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULE',
    'EQUALS_EQUALS',
    'EQUALS',
    'LPAREN',  # 'left parenthesis'
    'RPAREN',
    'LCBRACKET',  # 'left curly bracket'
    'RCBRACKET',
    'LBRACKET',
    'RBRACKET',
    'LTE',  # 'less than or equal'
    'LT',
    'GTE',
    'GT',
    'END'  # end of line
] + list(reserved.values())  # Add reserved words into tokens' list

# Regular expression rules for simple tokens
t_PLUS = r'\+'  # Recognizes a PLUS as a +
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\\'
t_MODULE = r'%'
t_EQUALS_EQUALS = r'=='  # '==' must be set before '!='
t_EQUALS = r'!='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCBRACKET = r'{'
t_RCBRACKET = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r']'
t_LTE = r'<='
t_LT = r'<'
t_GTE = r'>='
t_GT = r'>'
t_END = r'\;'
t_ignore = r' '  # Ignores spaces


# Regular expression rules for complex tokens

# Floats must be set before ints
def t_FLOAT(t):
    r'\d\.\d+'
    t.value = float(t.value)
    return t


# Floats must be set before ints
def t_FLOAT_CONSTANT(t):
    r'\d\.\d+'
    t.value = float(t.value)
    return t


# Ints must be set after floats
def t_INT(t):
    r'\d+'  # Any characters whose length is more than 0
    t.value = int(t.value)
    return t


def t_INT_CONSTANT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'  # The first char has to be a letter
    t.type = reserved.get(t.value, 'IDENT')  # Check for reserved words
    return t


def t_STRING(t):
    r'".*"'
    t.type = reserved.get(t.value, 'IDENT')
    return t


def t_STRING_CONSTANT(t):
    r'".*"'  # The first char has to be a letter
    t.type = reserved.get(t.value, 'IDENT')  # Check for reserved words
    return t


def t_COMMENT(t):
    r'\#.*'
    pass  # No return value. Token discarded


# Track row
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    raise SyntaxError('Error at line %d, position %d' % (t.lineno, t.lexpos))


lexer = lex.lex()  # Creates lex

# Receive input from the program
lexer.input('(1.2 + 2) * 4 {} break new new read >= <=')

while True:  # Prints the tokens
    tok = lexer.token()
    if not tok:
        break
    print(tok)
