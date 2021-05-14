from vlant.expr import lcc_to_py
from vlant.node import Node


class FuncDecl(Node):

    def __init__(self, name, block, params=[]):
        super(FuncDecl, self).__init__()
        self.name = name
        self.block = block
        if params is None:
            params = []
        self.params = params

    def validate(self, scope=None):
        for statement in self.block:
            statement.validate()

        for p in self.params:
            p.validate()


class VarDecl(Node):

    def __init__(self, _type, name, dims=[]):
        super(VarDecl, self).__init__()
        self.type = lcc_to_py[_type.upper()]
        self.name = name
        self.dims = dims

    def validate(self, scope=None):
        # TODO: check if variable was not declared before
        pass
