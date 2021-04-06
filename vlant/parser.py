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
        ...
    else:
        p[0] = p[1]


def p_funclist(p):
    '''
    funclist : funcdef funclist_
    '''
    p[0] = [p[1]] + [p[2]]


def p_funclist_(p):
    '''
    funclist_ : funclist
              |
    '''
    if len(p) == 2:
        p[0] = p[1]


def p_funcdef(p):
    '''
    funcdef : DEF IDENT LPAREN paramlist RPAREN LCBRACKET statelist RCBRACKET
    '''
    p[0] = [p[4]] + [p[6]]


def p_paramlist(p):
    '''
    paramlist : INT IDENT paramlist_
              | FLOAT IDENT paramlist_
              | STRING IDENT paramlist_
              |
    '''
    if p[1] is None:
        pass
    else:
        p[0] = p[3]


def p_paramlist_(p):
    '''
    paramlist_ : COMMA paramlist
               |
    '''
    if len(p) == 3:
        p[0] = p[2]
    else:
        pass


# TODO: break, for, readstat, print
def p_statement(p):
    '''
    statement : vardecl SEMICOLON
              | atribstat SEMICOLON
              | returnstat SEMICOLON
              | ifstat
              | LCBRACKET statelist RCBRACKET
              | SEMICOLON
    '''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1]
    elif len(p) == 4:
        p[0] = p[2]


def p_vardecl(p):
    '''
    vardecl : INT IDENT int_const_list
            | FLOAT IDENT float_const_list
            | STRING IDENT STRING_CONSTANT
    '''
    if p[1] != 'string':
        p[0] = p[3]


#def p_printstat(p):
#    '''
#    printstat : PRINT expression
#    '''
#    p[0] = p[2]


#def p_readstat(p):
#    '''
#    readstat : READ lvalue
#    '''
#    p[0] = p[2]


def p_int_const_list(p):
    '''
    int_const_list : INT_CONSTANT int_const_list
                   |
    '''
    if len(p) == 3:
        p[0] = p[2]


def p_float_const_list(p):
    '''
    float_const_list : FLOAT_CONSTANT float_const_list
                     |
    '''
    if len(p) == 3:
        p[0] = p[2]


def p_atribstat(p):
    '''
    atribstat : lvalue ASSIGN atribstat_
    '''
    p[0] = p[1] + p[3]


# TODO
def p_atribstat_(p):
    '''
    atribstat_ : INT_CONSTANT
    '''
    #if len(p) == 2:
    #    p[0] = p[1]
    #else:
    pass


# TODO check term_ or term
def p_term(p):
    '''
    term : unaryexpr term_
    '''
    p[0] = [p[1]] + [p[2]]


def p_term_(p):
    '''
    term_ : MULTIPLY term
          | DIVIDE term
          | MOD term
          |
    '''
    if len(p) == 3:
        p[0] = p[2]


# TODO + factor | - factor
def p_unaryexpr(p):
    '''
    unaryexpr : factor
    '''
    p[0] = p[1]


#def p_funccall(p):
#    '''
#    funccal : IDENT '(' paramlistcall ')'
#    '''
#    pass


def p_returnstat(p):
    '''
    returnstat : RETURN IDENT
               | RETURN
    '''
    ...


#TODO: add ifstat_ in the end
def p_ifstat(p):
    '''
    ifstat : IF LPAREN expression RPAREN statement
    '''
    p[0] = [p[3]] + [p[5]]


def p_statelist(p):
    '''
    statelist : statement
              | statement statelist
    '''
    p[0] = p[1]
    if len(p) == 3 and p[2] is not None:
        p[0] += p[2]


def p_expression(p):
    '''
    expression : numexpression expression_
    '''
    if p[1] != None:
        p[0] = p[1] + p[2]


# TODO complete with the other rules
def p_expression_(p):
    '''
    expression_ : GT expression_lte_gte
    '''
    p[0] = [2]


def p_expression_lte_gte(p):
    """
    expression_lte_gte : ASSIGN numexpression
                       | numexpression
    """
    if len(p) == 3:
        p[0] = p[2]
    else:
        p[0] = p[1]



# TODO: complete with numexpression_
def p_numexpression(p):
    '''
    numexpression : term
    '''
    p[0] = p[1]


def p_lvalue(p):
    """
    lvalue : IDENT lvalue_
    """
    p[0] = p[2]


# TODO NUM_EXPR_LIST
def p_lvalue_(p):
    """
    lvalue_ :
    """
    pass


# TODO (NUMEXPRESSION)
def p_factor(p):
    '''
    factor : INT_CONSTANT
           | FLOAT_CONSTANT
           | STRING_CONSTANT
           | lvalue
           | NULL
    '''
    # this is ugly
    input_type = type(p[1])
    if (input_type is not int) and (input_type is not float):
        if p[1] != 'null':
            p[0] = p[1]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! ", p)


def create_parser(debug=True):
    return yacc.yacc(debug=debug)

