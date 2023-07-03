class Point:
    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color


points = [Point(i + 1, i + 2) for i in range(0, 1000, 2)]
points[1].color = "yellow"

