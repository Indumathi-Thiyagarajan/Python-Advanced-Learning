import math
class Polygon:
    def __init__(self, n, R):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        
    def interior_angle(self):
        return (self._n -2) * 180 / self._n
    
    def edge_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    def area(self):
        return self._n / 2 * self.edge_length() * self.apothem()    
    
    def perimeter(self):     
        return self._n * self.edge_length()
    
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    def __eq__(self, other):
        if isinstance(other, Polygon):
            return (self._n == other._n and self._R == other._R)
        else:
            return NotImplemented
    def __gt__(self,other):
        if isinstance(other, Polygon):
            return (self._n > other._n)
        else:
            return NotImplemented
