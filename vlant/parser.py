import ply.yacc as yacc

from vlant.lexer import tokens


#def p_empty(p):
#    ''' empty : '''
#    pass


def p_program(p):
    '''
    program : statement
            | funclist
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


# TODO: FLOAT e STRING
def p_paramlist(p):
    '''
    paramlist : INT IDENT paramlist_
              |
    '''
    if p[1] is None:
        p[0] = ''
    else:
        p[0] = p[1] + p[2] + p[3]


def p_paramlist_(p):
    '''
    paramlist_ : COMMA paramlist
               |
    '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        pass

# TODO: printstat, readstat, BREAK, forstat, ifstat
def p_statement(p):
    '''
    statement : vardecl SEMICOLON
              | atribstat SEMICOLON
              | returnstat SEMICOLON
              | ifstat
              | LCBRACKET statelist RCBRACKET
              | SEMICOLON
    '''
    if len(p) == 3:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]


#TODO: complete with the other rules
def p_vardecl(p):
    '''
    vardecl : INT IDENT INT_CONSTANT
    '''
    p[0] = p[3]


def p_atribstat(p):
    '''
    atribstat : lvalue '=' atribstat_
    '''
    p[0] = p[1] + p[3]


# TODO: add lvalue_ in the end
def p_lvalue(p):
    '''
    lvalue : IDENT
    '''
    pass

# TODO complete with allocexpression and funccall
def p_atribstat_(p):
    '''
    atribstat_ : expression
    '''
    p[0] = p[1]


#def p_funccall(p):
#    '''
#    funccal : IDENT '(' paramlistcall ')'
#    '''
#    pass


def p_returnstat(p):
    '''
    returnstat : RETURN
    '''
    ...


#TODO: add ifstat_ in the end
def p_ifstat(p):
    '''
    ifstat : IF LPAREN expression RPAREN statement
    '''
    p[0] = p[3] + p[5] + p[6]


def p_statelist(p):
    '''
    statelist : statement
              | statement statelist
    '''
    p[0] = p[1]
    if len(p) == 3:
        p[0] += p[2]


def p_expression(p):
    '''
    expression : numexpression expression_
    '''
    p[0] = p[1] + p[2]


# TODO complete with the other rules
def p_expression_(p):
    '''
    expression_ : GTE
    '''
    pass


# TODO: to complete
def p_numexpression(p):
    '''
    numexpression : term
    '''
    p[0] = p[1]


# TODO to complete
def p_term(p):
    '''
    term : factor
    '''
    p[0] = p[1]


# TODO to complete
def p_factor(p):
    '''
    factor : INT_CONSTANT
    '''
    pass

# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


def create_parser():
    return yacc.yacc()

