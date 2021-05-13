from vlant.node import Node


class Var(Node):

    def __init__(self, name, dims=[]):
        super(Var, self).__init__()
        self.name = name
        self.dims = dims

    def validate(self, scope=None):
        pass
