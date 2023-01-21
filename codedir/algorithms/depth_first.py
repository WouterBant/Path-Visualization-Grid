from .breadth_first import BreadthFirst


class DepthFirst(BreadthFirst):

    def __init__(self, row, col):
        BreadthFirst.__init__(row, col)

    def getNextPosition(self):
        return self.q.pop()
    