import ply.yacc as yacc

from vlant.decl import FuncDecl, VarDecl
from vlant.expr import BinOp, Literal
from vlant.lexer import tokens
from vlant.statements import For, Assignment, Block
from vlant.values import Var


def p_program(p):
    """
    program : statement
            | funclist
    """
    if p[1] is None:
        ...
    else:
        p[0] = p[1]


def p_funclist(p):
    """
    funclist : funcdef funclist
             | funcdef
    """
    if len(p) == 3:
        p[0] = [p[1]] + p[2]
    else:
        p[0] = [p[1]]


def p_funcdef(p):
    """
    funcdef : DEF IDENT LPAREN paramlist RPAREN LCBRACKET statelist RCBRACKET
    """
    p[0] = FuncDecl(p[4], p[7])


def p_paramlist(p):
    """
    paramlist : INT IDENT paramlist_
              | FLOAT IDENT paramlist_
              | STRING IDENT paramlist_
              |
    """
    if len(p) == 4:
        p[0] = p[3]


def p_paramlist_(p):
    """
    paramlist_ : COMMA paramlist
               |
    """
    if len(p) == 3:
        p[0] = p[2]


def p_statement(p):
    """
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
    """
    if len(p) == 4:
        p[0] = p[2]
    else:
        p[0] = p[1]


def p_vardecl(p):
    """
    vardecl : INT IDENT
            | FLOAT IDENT
            | STRING IDENT
    """
    p[0] = VarDecl(p[1], p[2])


def p_printstat(p):
    """
    printstat : PRINT expression
    """
    p[0] = p[2]


def p_readstat(p):
    """
    readstat : READ lvalue
    """
    p[0] = p[2]


def p_atribstat(p):
    """
    atribstat : lvalue ASSIGN atribstat_
    """
    p[0] = Assignment(p[1], p[3])


def p_atribstat_(p):
    """
    atribstat_ : allocexpression
               | funccall
               | expression
    """
    p[0] = p[1]


def p_allocexpression(p):
    """
    allocexpression : NEW allocexpression_
    """
    p[0] = p[2]


# TODO: update string_constant rule for it to accept more than one string
def p_allocexpression_(p):
    """
    allocexpression_ : INT num_expr_list
                     | FLOAT num_expr_list
                     | STRING STRING_CONSTANT
    """
    if p[1] != 'string':
        p[0] = p[2]


# TODO check term_ or term
def p_term(p):
    """
    term : unaryexpr MULTIPLY term
         | unaryexpr DIVIDE term
         | unaryexpr MOD term
         | unaryexpr
    """
    if len(p) == 4:
        p[0] = BinOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]


def p_unaryexpr(p):
    """
    unaryexpr : factor PLUS factor
              | factor MINUS factor
              | factor
    """
    if len(p) == 4:
        p[0] = BinOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]


def p_funccall(p):
    """
    funccall : IDENT LPAREN paramlistcall RPAREN
    """
    p[0] = p[3]


def p_paramlistcall(p):
    """
    paramlistcall : IDENT paramlistcall_
                  |
    """
    if len(p) == 3:
        p[0] = p[2]


def p_paramlistcall_(p):
    """
    paramlistcall_ : COMMA paramlistcall
                   |
    """
    if len(p) == 3:
        p[0] = p[2]


def p_returnstat(p):
    """
    returnstat : RETURN IDENT
               | RETURN
    """
    ...


def p_ifstat(p):
    """
    ifstat : IF LPAREN expression RPAREN statement ifstat_
    """
    p[0] = [p[3]] + [p[5]] + [p[6]]


def p_ifstat_(p):
    """
    ifstat_ : ELSE statement
            |
    """
    if len(p) == 3:
        p[0] = p[2]


def p_forstat(p):
    """
    forstat : FOR LPAREN atribstat SEMICOLON expression SEMICOLON atribstat RPAREN statement
    """
    p[0] = For(p[3], p[5], p[7], p[9])


def p_statelist(p):
    """
    statelist : statement statelist
              | statement
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[2]


def p_expression(p):
    """
    expression : numexpression GT numexpression
                | numexpression GTE numexpression
                | numexpression LT numexpression
                | numexpression LTE numexpression
                | numexpression EQUALS numexpression
                | numexpression NOT_EQUAL numexpression
                | numexpression
    """
    if len(p) == 4:
        p[0] = BinOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]


def p_numexpression(p):
    """
    numexpression : term PLUS term
                  | term MINUS term
                  | term
    """
    if len(p) == 4:
        p[0] = BinOp(p[1], p[2], p[3])
    else:
        p[0] = p[1]


# TODO / WARN: ambiguity?
def p_lvalue(p):
    """
    lvalue : IDENT num_expr_list
           | IDENT
    """
    if len(p) == 3:
        p[0] = Var(p[1], dims=p[2])
    else:
        p[0] = Var(p[1])


def p_num_expr_list(p):
    """
    num_expr_list : LBRACKET numexpression RBRACKET num_expr_list_
    """
    p[0] = p[1] + [p[2]]


def p_num_expr_list_(p):
    """
    num_expr_list_ : num_expr_list
                   |
    """
    if len(p) == 2:
        p[0] = p[1]


def p_factor(p):
    """
    factor : INT_CONSTANT
           | FLOAT_CONSTANT
           | STRING_CONSTANT
           | lvalue
           | NULL
           | LPAREN numexpression RPAREN
    """
    if len(p) == 4:
        p[0] = p[2]
    else:
        if type(p[1]) is type(Var):
            p[0] = p[1]
        else:
            p[0] = Literal(p[1])


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input! ", p)


def create_parser(debug=True):
    return yacc.yacc(debug=debug)
