import ply.yacc as yacc

from calclex import tokens
from ce.semantic.declarations import DeclVariable, DeclFunction


def p_empty(p):
    ''' empty : '''
    pass


def p_program(p):
    '''
    program : statement
            | funclist
            | empty
    '''
    if p[1] is None:
        ...  # ?
    else:
        p[0] = p[1]


def p_funclist(p):
    '''
    funclist : funcdef funclist
             | funcdef
    '''
    if len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1]


def p_funcdef(p):
    '''
    funcdef : DEF IDENT '(' paramlist ')' '{' statelist '}'
    '''
    p[0] = DeclFunction(p[1], p[2], args=p[4])


def p_paramlist(p):
    '''
    paramlist : INT IDENT ',' paramlist
              | FLOAT IDENT ',' paramlist
              | STRING IDENT ',' paramlist
              | INT IDENT
              | FLOAT IDENT
              | STRING IDENT
              | empty
    '''
    if p[1] is None:
        ...  # ?
    elif len(p) == 3:
        p[0] = p[1] + p[2]
    else:
        p[0] = p[1] + p[2] + p[4]


def p_statement(p):
    '''
    statement : vardecl ';'
              | atribstat ';'
              | printstat ';'
              | readstat ';'
              | returnstat ';'
              | ifstat
              | forstat
              | {statelist}
              | BREAK ';'
              | ';'
    '''
    p[0] = p[1]


def p_vardecl(p):
    '''
    vardecl : INT IDENT int_const_list
            | FLOAT IDENT int_const_list
            | STRING IDENT int_const_list
    '''
    p[0] = DeclVariable(p[1], p[2], p[3])  # TODO: check this, ignored int_const_list
                                           # the given grammar is weird in relation to this


def p_atribstat(p):
    '''
    atribstat : lvalue = expression
              | lvalue = ...
              | lvalue = ...
    '''
    # TODO: this rule cannot be implemented yet, because it can be factored
    ...


def p_funccall(p):
    '''
    funccal : IDENT '(' paramlistcall ')'
    '''
    pass


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")

# Build the parser
parser = yacc.yacc()

while True:
   try:
       s = input('calc > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print(result)

