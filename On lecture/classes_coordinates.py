class Coordinate(object):
    def __init__(self, xval,yval):
        self.x = xval
        self.y = yval
    def distance(self, other):
        x_diff_sq = (self.x-other.x) ** 2
        y_diff_sq = (self.y-other.y) ** 2
        return (x_diff_sq + y_diff_sq) ** 0.5
c = Coordinate(7,8)
orig = Coordinate(-4,-3)
print(c.distance(orig))