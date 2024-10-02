from objective1 import Polygon
from objective2 import Polygon_sequence

interior_angle = Polygon(3, 10).interior_angle()
edge_length = Polygon(3, 10).edge_length()
apothem = Polygon(3, 10).apothem()
area = Polygon(3, 10).area()
perimeter = Polygon(3, 10).perimeter()
print(f"interior_angle:{interior_angle}, edge_length:{edge_length}, apothem:{apothem}, area:{area}, perimeter:{perimeter}")

poly1 = Polygon(3, 10)
poly2 = Polygon(4, 5)
poly3 = Polygon(3, 10)
print(poly1 == poly2)
print(poly1 == poly3)
print(poly1 > poly2)

max_efficiency_polygon = Polygon_sequence(n=25).max_efficiency_polygon()
print(max_efficiency_polygon)

# Example usage
polygon_seq = Polygon_sequence(5)
print(f"length of polygon sequence : {len(polygon_seq)}")  # Output: 3
print(f" get 0th item of polygon sequence : {polygon_seq[0]}")  
