import ply.lex as lex


# Create reserved words
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',
    'const int': 'INT_CONSTANT',
    'const float': 'FLOAT_CONSTANT',
    'const string': 'STRING_CONSTANT',

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
    'LITERAL_FLOAT',
    'LITERAL_INT',
    'LITERAL_STRING',
    'IDENT',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MODULE',
    'EQUALS',
    'ASSIGN',
    'NOT_EQUAL',
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
    'SEMICOLON',
    'COMMA'
] + list(reserved.values())  # Add reserved words into tokens' list

# Regular expression rules for simple tokens
t_PLUS = r'\+'  # Recognizes a PLUS as a +
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\\'
t_MODULE = r'%'
t_EQUALS = r'=='  # '==' must be set before '!='
t_ASSIGN = r'='
t_NOT_EQUAL = r'!='
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
t_SEMICOLON = r'\;'
t_COMMA = r','
t_ignore = r' '  # Ignores spaces


# Regular expression rules for complex tokens

# Floats must be set before ints
def t_LITERAL_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


# Ints must be set after floats
def t_LITERAL_INT(t):
    r'\d+'  # Any numeric character whose length is more than 0
    t.value = int(t.value)
    return t


def t_LITERAL_STRING(t):
    r'".*"'
    t.type = reserved.get(t.value, 'STRING')  # Check for reserved words
    return t


def t_IDENT(t):
    r'[a-zA-Z_]+[a-zA-Z0-9_]*'  # The first char has to be a letter
    t.type = reserved.get(t.value, 'IDENT')
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

# Receive input
# executa as:
#   python3 main.py
#   file_name
file_name = input()
f = open(file_name, 'r')
data = f.read()
lexer.input(data)

while True:  # Prints the tokens
    tok = lexer.token()
    if not tok:
        break
    print(tok)
