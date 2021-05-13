from vlant.node import Node


class For(Node):
    def __init__(self, decl, cond, step, block):
        super(For, self).__init__()
        self.decl = decl
        self.cond = cond
        self.step = step
        self.block = block

    def validate(self, scope=None):
        pass


class Assignment(Node):

    def __init__(self, var, expr):
        super(Assignment, self).__init__()
        self.var = var
        self.expr = expr

    def validate(self, scope=None):
        # TODO: validate expr type against var type (should be compatible)
        self.var.validate()
        self.expr.validate()


class Block(Node):

    def __init__(self, statements=[]):
        super(Block, self).__init__()
        self.statements = statements

    def validate(self, scope=None):
        for statement in self.statements:
            statement.validate(scope)
