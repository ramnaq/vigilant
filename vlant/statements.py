from vlant.node import Node
from vlant.scope import Scopes


class Main(Node):
    def __init__(self, statements=[]):
        self.statements = statements

    def validate(self, scope=None):
        scope = Scopes()
        with scope() as s:
            for c in self.statements:
                c.validate(s)


class For(Node):
    def __init__(self, decl, cond, step, block):
        super(For, self).__init__()
        self.decl = decl
        self.cond = cond
        self.step = step
        self.block = block

    def validate(self, scope):
        with scope() as scope_:
            self.decl.validate(scope_)
            cond = If(self.cond, self.block, else_block=[])
            cond.validate(scope_)
            self.step.validate(scope_)


class If(Node):
    def __init__(self, cond, block, else_block):
        super(If, self).__init__()
        self.cond = cond
        self.block = block
        self.else_block = else_block

    def validate(self, scope):
        self.cond.validate(scope)

        if self.cond.type == 'STRING':
            raise Exception('Type error: "if" condition cant be of type STRING!')

        # If scope
        with scope() as scope_:
            # TODO turn into Block
            for statement in self.block:
                statement.validate(scope_)

        # Else scope
        if self.else_block is not None:
            if type(self.else_block) is not list:
                self.else_block = [self.else_block]

            with scope() as scope_:
                # TODO turn into Block
                for statement in self.else_block:
                    statement.validate(scope)


class Assignment(Node):

    def __init__(self, var, expr):
        super(Assignment, self).__init__()
        self.var = var
        self.expr = expr

    def validate(self, scope):
        # TODO: validate expr type against var type (should be compatible)
        self.var.validate(scope)
        self.expr.validate(scope)


class Block(Node):

    def __init__(self, statements=[]):
        super(Block, self).__init__()
        self.statements = statements

    def validate(self, scope=None):
        for statement in self.statements:
            statement.validate(scope)


class Return(Node):
    def __init__(self, value=None):
        self.value = value

    def validate(self, scope):
        if self.value is None:
            return
        self.value.validate(scope)
