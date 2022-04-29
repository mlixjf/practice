import math
from operator import methodcaller

class Point:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%r, %r)" % (self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


if __name__ == '__main__':
    p = Point(0, 0)
    print(getattr(p, "distance")(1, 1))

    distance = methodcaller("distance", 3, 4)
    print(distance(p))
    points = [
        Point(1, 2),
        Point(3, 0),
        Point(10, -3),
        Point(-5, -7),
        Point(-1, 8),
        Point(3, 2)
    ]

    points.sort(key=methodcaller("distance", 0, 0))
    print(points)