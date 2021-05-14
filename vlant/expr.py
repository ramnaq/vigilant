from vlant.errors import IncompatibleTypesException, UnsupportedOperandException
from vlant.node import Node


lcc_to_py = {
    'INT': int,
    'FLOAT': float,
    'STRING': str
}


class BinOp(Node):

    def __init__(self, left, op, right):
        super(BinOp, self).__init__()
        self.left = left
        self.op = op
        self.right = right

    def validate(self, scope=None):
        self.left.validate()
        self.right.validate()

        a_type = self.left.type
        b_type = self.right.type
        if self.left.type != self.right.type:
            raise IncompatibleTypesException(f'TypeError: incompatible types '
                                             f'{a_type} {self.op} {b_type}')
        if a_type == str or b_type == str:
            if not self.valid_str_op():
                raise UnsupportedOperandException(
                    f'TypeError: unsupported operand {self.op.value} for type str')
        pass

    def valid_str_op(self):
        return (self.op.value == '+') or (self.op.value == '*')


class Literal(Node):

    def __init__(self, value):
        self.value = value

    def validate(self, scope=None):
        pass


class FuncCall(Node):
    def __init__(self, name, params=[]):
        super(FuncCall, self).__init__()
        self.name = name
        self.params = params

    def validate(self, scope=None):
        pass
