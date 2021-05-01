# Membros do grupo:
# Letícia do Nascimento (16104595)
# Ramna Sidharta (16100742)
# Matheus Schaly (18200436)

import json
import ply.lex as lex

# Create reserved words
reserved = {
    'int': 'INT',
    'float': 'FLOAT',
    'string': 'STRING',

    'if': 'IF',
#    'then': 'THEN',
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
    'FLOAT_CONSTANT',
    'INT_CONSTANT',
    'STRING_CONSTANT',
    'IDENT',
    'PLUS',
    'MINUS',
    'MULTIPLY',
    'DIVIDE',
    'MOD',
    'EQUALS',
    'ASSIGN',
    'NOT_EQUAL',
    'LPAREN',  # 'left parenthesis'
    'RPAREN',
    'LCBRACKET',  # 'left curly bracket'
    'RCBRACKET',
    'LBRACKET',
    'RBRACKET',
#    'LTE',  # 'less than or equal'
    'LT',
#    'GTE',
    'GT',
    'SEMICOLON',
    'COMMA'
] + list(reserved.values())  # Add reserved words into tokens' list

# Regular expression rules for simple tokens
t_PLUS = r'\+'  # Recognizes a PLUS as a +
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'\\'
t_MOD = r'%'
t_EQUALS = r'=='  # '==' must be set before '!='
t_ASSIGN = r'='
t_NOT_EQUAL = r'!='
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LCBRACKET = r'{'
t_RCBRACKET = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r']'
#t_LTE = r'<='
t_LT = r'<'
#t_GTE = r'>='
t_GT = r'>'
t_SEMICOLON = r'\;'
t_COMMA = r','
t_ignore = r' '  # Ignores spaces

literals = [',', ';', '(', ')', '{', '}', '+', '-', '*', '%', '/']

# Regular expression rules for complex tokens

# Floats must be set before ints
def t_FLOAT_CONSTANT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t


# Ints must be set after floats
def t_INT_CONSTANT(t):
    r'\d+'  # Any numeric character whose length is more than 0
    t.value = int(t.value)
    return t


def t_STRING_CONSTANT(t):
    r'"[^"]*"'
    val = t.value
    t.value = str(val[1:len(val)-1]).encode()
    return t


def t_IDENT(t):
    r'[a-zA-Z_]+[a-zA-Z0-9_]*'  # The first char has to be a letter
    t.type = reserved.get(t.value, 'IDENT')
    if t.value in t.lexer.symbol_table:
        # Add occurrence to symbol already present in the table
        existing_symbol = t.lexer.symbol_table[t.value]
        symbol_occurrences = existing_symbol[1]
        symbol_occurrences.append((t.lineno, t.lexpos))
    else:
        # Add new symbol to the table
        t.lexer.symbol_table[t.value] = (t.type, [(t.lineno, t.lexpos)])
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


lexer = lex.lex()
lexer.symbol_table = {}


if __name__ == '__main__':
    lex.runmain(lexer=lexer)

    print('\n#####################')
    print('\nSymbol table: ')
    print(json.dumps(lexer.symbol_table))

