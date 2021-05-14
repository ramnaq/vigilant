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


class If(Node):
    def __init__(self, cond, block, else_block):
        super(If, self).__init__()
        self.cond = cond
        self.block = block
        self.else_block = else_block

    def validate(self, scope=None):
        self.cond.validate()

        if self.cond.type == 'STRING':
            raise Exception('Type error: "if" condition cant be of type STRING')

        for statement in self.block:
            statement.validate()

        if self.else_block is not None:
            if type(self.else_block) is not list:
                self.else_block = [self.else_block]
            for statement in self.else_block:
                statement.validate()


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


class Return(Node):
    def __init__(self, value=None):
        self.value = value

    def validate(self, scope=None):
        if self.value is None:
            return
        self.value.validate()
