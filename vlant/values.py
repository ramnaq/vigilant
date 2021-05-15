from vlant.errors import VarDeclException, ArrayAccessException
from vlant.node import Node


class Var(Node):

    def __init__(self, name, dims=[]):
        super(Var, self).__init__()
        self.name = name
        self.dims = dims

    def validate(self, scope):
        var = scope.get(self.name)
        if var is None:
            raise VarDeclException(f'NameError: variable "{self.name}" not '
                                   f'declared!')
        # if len(var.dims) < len(self.dims):
        #     raise ArrayAccessException(
        #         f'Trying to access bigger array dimensions! Var "{self.name}"'
        #         f' has {len(var.dims)} dimensions, but trying to access'
        #         f'  {len(self.dims)}.')
        self.type = var.type


class Literal(Node):

    def __init__(self, value):
        super(Literal, self).__init__()
        self.value = value
        self.type = type(self.value)

    def validate(self, scope):
        pass

