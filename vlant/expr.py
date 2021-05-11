from vlant.node import Node


class BinOp(Node):

    def __init__(self, left, op, right):
        super(BinOp, self).__init__()
        self.left = left
        self.op = op
        self.right = right

    def validate(self, scope):
        pass


class Number(Node):

    def __init__(self,value):
        self.value = value