

import math

class Polygon:
    """Rule of thumb to convert iter to lazyiter :

Converting an iterable to an iterator is as simple as using iter() on an iterable. 
For laziness, you can go the generator route or implement __iter__ and __next__ in your class. 
In either case, you’d be managing the iteration with an index or a similar mechanism.
It ensures you can keep track of your position in the sequence, yielding one element at a time without loading everything into memory
"""
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
    
    @property
    def edge_length(self):
        return 2 * self._R * math.sin(math.pi / self._n)
    
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
# lazy iteration using generator

class Polygon_lazyiter_gen:
    def __init__(self, n, R=10):
        self._n = n
        self._R = R
        # current index is not initiated
    def __iter__(self):
        return self._generator()
    def _generator(self):
        for i in range(3, self._n + 1):
            yield Polygon(i, self._R)#explanation below
        #Tuples: Initialize with default values if you need to update them during iteration.
        #Lists: Can start empty and be dynamically updated during iteration.
    def max_efficiency_polygon(self):
        efficiency_list = (None, 0)
        for polygon in self:
            area = polygon.area
            perimeter = polygon.perimeter
            efficiency = area / perimeter
            efficiency_list = ((polygon._n, efficiency) if not efficiency_list or efficiency > efficiency_list[1] else efficiency_list)
        return f"Polygon with {efficiency_list[0]} edges and {self._R} has maximum efficiency"


class Polygon_lazyiter:
    """ iterator based class
* Initialization:
The Polygon_iter class does not create a list of polygons upfront. Instead, it initializes an index to keep track of the current polygon.
The index starts at 3 because polygons with fewer than 3 sides are not valid.
Initialization:

Initialize _current to keep track of the current position in the iteration.

Remove Precomputed List:

Instead of precomputing and storing all polygons, we generate them on-the-fly.

Implement __iter__:

Returns self because this object itself is an iterator.

Implement __next__:

Generates the next polygon and increments the _current counter.

Raises StopIteration when the end is reached.

when next is there we return self. when next is not there we return self og iterator"""

class Polygon_lazyiter_next:
    def __init__(self, n, R=10):
        if n < 3:
            raise ValueError('Polygon must have at least 3 vertices.')
        self._n = n
        self._R = R
        self._current = 3
    
    def max_efficiency_polygon(self):
        efficiency_list = (None, 0)
        for polygon in self:
            area = polygon.area
            perimeter = polygon.perimeter
            efficiency = area / perimeter
            efficiency_list = (polygon._n, efficiency) if not efficiency_list or efficiency > efficiency_list[1] else efficiency_list
        return f"Polygon with {efficiency_list[0]} edges and {self._R} has maximum efficiency"
    
    def __repr__(self):
        return f'Polygon_sequence(n={self._n}, R={self._R}, max_efficiency_polygon={self.max_efficiency_polygon()})'
    
    def __len__(self):
        return self._n - 2
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self._current > self._n:
            raise StopIteration
        else:
            polygon = Polygon(self._current, self._R)
            self._current += 1
            return polygon
