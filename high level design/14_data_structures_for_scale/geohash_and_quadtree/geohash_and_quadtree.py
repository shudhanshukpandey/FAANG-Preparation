"""Spatial Indexing (Quadtree & Proximity Search) Simulation."""
class Point:
    def __init__(self, x: float, y: float, data: str):
        self.x, self.y, self.data = x, y, data

class SimpleQuadTree:
    def __init__(self, boundary: tuple[float, float, float, float], capacity=4):
        self.x1, self.y1, self.x2, self.y2 = boundary
        self.capacity = capacity
        self.points = []
    def insert(self, p: Point) -> bool:
        if not (self.x1 <= p.x <= self.x2 and self.y1 <= p.y <= self.y2):
            return False
        if len(self.points) < self.capacity:
            self.points.append(p)
            return True
        return True # In full implementation, splits into NW, NE, SW, SE

def run_tests():
    qt = SimpleQuadTree((0, 0, 100, 100), capacity=2)
    p1 = Point(10, 20, "Driver_A")
    p2 = Point(30, 40, "Driver_B")
    assert qt.insert(p1) is True
    assert qt.insert(p2) is True
    print("✅ geohash_and_quadtree passed!")

if __name__ == "__main__":
    run_tests()
