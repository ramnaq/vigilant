import ply.yacc as yacc

from vlant.lexer import tokens


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
    if len(p) == 4:
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


def p_statement(p):
    '''
    statement : vardecl SEMICOLON
              | atribstat SEMICOLON
              | printstat SEMICOLON
              | readstat SEMICOLON
              | returnstat SEMICOLON
              | ifstat
              | forstat
              | LCBRACKET statelist RCBRACKET
              | BREAK SEMICOLON
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
    vardecl : INT IDENT
            | FLOAT IDENT
            | STRING IDENT
    '''
    pass


def p_printstat(p):
    '''
    printstat : PRINT expression
    '''
    p[0] = p[2]


def p_readstat(p):
    '''
    readstat : READ lvalue
    '''
    p[0] = p[2]


def p_atribstat(p):
    '''
    atribstat : lvalue ASSIGN atribstat_
    '''
    p[0] = [p[1]] + [p[3]]


def p_atribstat_(p):
    '''
    atribstat_ : allocexpression
               | funccall
               | expression
    '''
    p[0] = p[1]


def p_allocexpression(p):
    '''
    allocexpression : NEW allocexpression_
    '''
    p[0] = p[2]


# TODO: update string_constant rule for it to accept more than one string
def p_allocexpression_(p):
    '''
    allocexpression_ : INT num_expr_list
                     | FLOAT num_expr_list
                     | STRING STRING_CONSTANT
    '''
    if p[1] != 'string':
        p[0] = p[2]


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


def p_unaryexpr(p):
    '''
    unaryexpr : factor
              | PLUS factor
              | MINUS factor
    '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_funccall(p):
    '''
    funccall : IDENT LPAREN paramlistcall RPAREN
    '''
    p[0] = p[3]


def p_paramlistcall(p):
    '''
    paramlistcall : IDENT paramlistcall_
                  |
    '''
    if len(p) == 3:
        p[0] = p[2]


def p_paramlistcall_(p):
    '''
    paramlistcall_ : SEMICOLON paramlistcall
                   |
    '''
    if len(p) == 3:
        p[0] = p[2]


def p_returnstat(p):
    '''
    returnstat : RETURN IDENT
               | RETURN
    '''
    ...


def p_ifstat(p):
    '''
    ifstat : IF LPAREN expression RPAREN statement ifstat_
    '''
    p[0] = [p[3]] + [p[5]] + [p[6]]


def p_ifstat_(p):
    '''
    ifstat_ : ELSE statement
            |
    '''
    if len(p) == 3:
        p[0] = p[2]


def p_forstat(p):
    '''
    forstat : FOR LPAREN atribstat COMMA expression COMMA atribstat RPAREN statement
    '''
    p[0] = p[3] + p[5] + p[7] + p[9]


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
    p[0] = [p[1]] + [p[2]]


def p_expression_(p):
    '''
    expression_ : GT expression_lte_gte
                | LT expression_lte_gte
                | EQUALS numexpression
                | NOT_EQUAL numexpression
                |
    '''
    if len(p) == 3:
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



def p_numexpression(p):
    '''
    numexpression : term numexpression_
    '''
    p[0] = [p[1]] + [p[2]]


def p_numexpression_(p):
    '''
    numexpression_ : PLUS term numexpression_
                   | MINUS term numexpression_
                   |
    '''
    if len(p) == 4:
        p[0] = [p[2]] + [p[3]]


def p_lvalue(p):
    """
    lvalue : IDENT lvalue_
    """
    p[0] = p[2]


def p_lvalue_(p):
    '''
    lvalue_ : num_expr_list
            |
    '''
    if len(p) == 2:
        p[0] = p[1]


def p_num_expr_list(p):
    '''
    num_expr_list : LBRACKET numexpression RBRACKET num_expr_list_
    '''
    p[0] = [p[1]] + [p[2]]


def p_num_expr_list_(p):
    '''
    num_expr_list_ : num_expr_list
                   |
    '''
    if len(p) == 2:
        p[0] = p[1]


def p_factor(p):
    '''
    factor : INT_CONSTANT
           | FLOAT_CONSTANT
           | STRING_CONSTANT
           | lvalue
           | NULL
           | LPAREN numexpression RPAREN
    '''
    if len(p) == 2:
        t = type(p[1])
        if (t is not str) and (t is not float) and (t is not int) and (t is not 'null'):
            p[0] = p[1]
    else:
        p[0] = p[2]


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! ", p)


def create_parser(debug=True):
    return yacc.yacc(debug=debug)

