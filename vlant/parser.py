import ply.yacc as yacc

from vlant.lexer import tokens


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
    p[0] = p[1] + p[2] + p[4] + p[7]


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
              | '{' statelist '}'
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
    p[0] = p[1] + p[2] + p[3]


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


def create_parser():
    return yacc.yacc()

