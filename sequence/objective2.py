from objective1 import Polygon
class Polygon_sequence:
    def __init__(self, n, R=10):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self.polygons = [Polygon(n,R) for n in range(3,n+1)]
        # print(self.polygons)
        #[Polygon(n=3, R=10), Polygon(n=4, R=10), Polygon(n=5, R=10), Polygon(n=6, R=10), Polygon(n=7, R=10), Polygon(n=8, R=10), Polygon(n=9, R=10), Polygon(n=10, R=10), Polygon(n=11, R=10), Polygon(n=12, R=10), Polygon(n=13, R=10), Polygon(n=14, R=10), Polygon(n=15, R=10), Polygon(n=16, R=10), Polygon(n=17, R=10), Polygon(n=18, R=10), Polygon(n=19, R=10), Polygon(n=20, R=10), Polygon(n=21, R=10), Polygon(n=22, R=10), Polygon(n=23, R=10), Polygon(n=24, R=10), Polygon(n=25, R=10)]
        
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
