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

    def validate(self, scope):
        self.left.validate(scope)
        self.right.validate(scope)

        a_type = self.left.type
        b_type = self.right.type
        if self.left.type != self.right.type:
            raise IncompatibleTypesException(f'TypeError: incompatible types '
                                             f'{a_type} {self.op} {b_type}!')
        if a_type == str or b_type == str:
            if not self.valid_str_op():
                msg = f'TypeError: unsupported operand "{self.op}" for type ' \
                      f'STRING_CONSTANT!'
                raise UnsupportedOperandException(msg)

        self.type = a_type

    def valid_str_op(self):
        return self.op in ['+', '*', '==']


class FuncCall(Node):
    def __init__(self, name, params=[]):
        super(FuncCall, self).__init__()
        self.name = name
        self.params = params

    def validate(self, scope):
        pass
