from vlant.errors import VarDeclException
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

    def validate(self, scope):
        if self.name in scope.current:
            raise VarDeclException(
                f'NameError: function {self.name} already declared!')

        scope[self.name] = self

        # Validate function block and args
        with scope() as scop:
            for arg in self.params:
                arg.validate(scop)
            for statement in self.block:
                statement.validate(scope)


class VarDecl(Node):

    def __init__(self, _type, name, dims=[]):
        super(VarDecl, self).__init__()
        self.type = lcc_to_py[_type.upper()]
        self.name = name
        self.dims = dims

    def validate(self, scope):
        if self.name in scope.current:
            raise VarDeclException(f'Variable "{self.name}" already declared!')

        scope[self.name] = self
