from objective1 import Polygon
class Polygon_sequence:
    def __init__(self, n, R=10):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self.polygons = [Polygon(n,R) for n in range(3,n+1)]
        
    def max_efficiency_polygon(self):
        efficiency_list = ()
        for polygon in self.polygons:
            area = polygon.area()
            perimeter = polygon.perimeter()
            efficiency = area/perimeter
            efficiency_list = ((polygon._n,efficiency) if not efficiency_list or efficiency > efficiency_list[1] else efficiency_list)
        return f"Polygon with {efficiency_list[0]} edges and {self._R} has maximum efficiency"
    
    def __repr__(self):
        return f'Polygon_sequence(n={self._n}, R={self._R}, max_efficiency_polygon={self.max_efficiency_polygon()})'
    
    def __len__(self):
        return len(self.polygons)
    
    def __getitem__(self, index):
        return self.polygons[index]
