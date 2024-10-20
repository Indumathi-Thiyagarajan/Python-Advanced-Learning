import math

class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n
    
    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return int((self._n - 2) * 180 / self._n)

    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges 
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
        
    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.count_vertices > other.count_vertices
        else:
            return NotImplemented
        
""" Transforming a sequence into an iterator in Python is quite straightforward. Here’s the playbook:

Identify your sequence: This could be a list, tuple, string, etc.

Use the iter() function: This built-in function converts your sequence into an iterator."""       
class Polygon_iter:
    def __init__(self, n, R=10):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self.polygons = [Polygon(n,R) for n in range(3,n+1)]
        
    def max_efficiency_polygon(self):
        efficiency_list = ()
        for polygon in self.polygons:
            area = polygon.area
            perimeter = polygon.perimeter
            efficiency = area/perimeter
            efficiency_list = ((polygon._n,efficiency) if not efficiency_list or efficiency > efficiency_list[1] else efficiency_list)
        return f"Polygon with {efficiency_list[0]} edges and {self._R} has maximum efficiency"
    
    def __repr__(self):
        return f'Polygon_sequence(n={self._n}, R={self._R}, max_efficiency_polygon={self.max_efficiency_polygon()})'
    
    def __len__(self):
        return len(self.polygons)
    
    def __getitem__(self, index):
        return self.polygons[index]
    
    def __iter__(self):
        return iter(self.polygons) #this convert a sequence into an iterator
