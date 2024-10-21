
import math
from polygon import Polygon
from polygon import Polygon_lazyiter_gen, Polygon_lazyiter_next
def test_polygon():
    abs_tol = 0.001
    rel_tol = 0.001
    
    try:
        p = Polygon(2, 10)
        assert False, ('Creating a Polygon with 2 sides: '
                       ' Exception expected, not received')
    except ValueError:
        pass
                       
    n = 3 
    R = 1
    p = Polygon(n, R)
    assert str(p) == 'Polygon(n=3, R=1)', f'actual: {str(p)}'
    print(f"test passed, {str(p)}")

    assert p.count_vertices == n, (f'actual: {p.count_vertices},'
                                   f' expected: {n}')
    print(f"test passed, {str(n)}")
    assert p.count_edges == n, f'actual: {p.count_edges}, expected: {n}'
    print(f"test passed, {str(p.count_edges)}")
    assert p.circumradius == R, f'actual: {p.circumradius}, expected: {n}'
    print(f"test passed, {str(p.circumradius)}")
    assert p.interior_angle == 60, (f'actual: {p.interior_angle},'
                                    ' expected: 60')
    print(f"test passed, {str(p.interior_angle)}")
    n = 4
    R = 1
    p = Polygon(n, R)
    assert p.interior_angle == 90, (f'actual: {p.interior_angle}, '
                                    ' expected: 90')
    assert math.isclose(p.area, 2, 
                        rel_tol=abs_tol, 
                        abs_tol=abs_tol), (f'actual: {p.area},'
                                           ' expected: 2.0')
    print(f"test passed",{p.area})
    assert math.isclose(p.side_length, math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.side_length},'
                                          f' expected: {math.sqrt(2)}')
    print(f"test passed",{p.side_length})
    assert math.isclose(p.perimeter, 4 * math.sqrt(2),
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                          f' expected: {4 * math.sqrt(2)}')
    print(f"test  passed",{p.perimeter})
    assert math.isclose(p.apothem, 0.707,
                       rel_tol=rel_tol,
                       abs_tol=abs_tol), (f'actual: {p.perimeter},'
                                     ' expected: 0.707')
    print(f"test passed", {p.perimeter}) 
    p = Polygon(6, 2)
    assert math.isclose(p.side_length, 2,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed", p.side_length)
    assert math.isclose(p.apothem, 1.73205,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed", p.apothem)
    assert math.isclose(p.area, 10.3923,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print('test passed", p.area)')
    assert math.isclose(p.perimeter, 12,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed ", p.perimeter)
    assert math.isclose(p.interior_angle, 120,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed", p.interior_angle)
    
    p = Polygon(12, 3)
    assert math.isclose(p.side_length, 1.55291,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed", p.side_length)
    assert math.isclose(p.apothem, 2.89778,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed", p.apothem)
    assert math.isclose(p.area, 27,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed",  p.area)
    assert math.isclose(p.perimeter, 18.635,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed",  p.perimeter)
    assert math.isclose(p.interior_angle, 150,
                        rel_tol=rel_tol, abs_tol=abs_tol)
    print("test passed" ,  p.interior_angle)
    
    p1 = Polygon(3, 10)
    p2 = Polygon(10, 10)
    p3 = Polygon(15, 10)
    p4 = Polygon(15, 100)
    p5 = Polygon(15, 100)

    assert p2 > p1
    print("test passed, p2 > p1")
    assert p2 < p3
    print("test passed, p2 < p3")
    assert p3 != p4
    print("test passed , p3 != p4")
    assert p1 != p4
    print("test passed, p1 != p4")
    assert p4 == p5
    print("test passed",  p4 == p5)
    import time
    print("******** using generator as lazy iterator")
    start = time.time()
    print("start time:", start)
    max_efficiency_polygon = Polygon_lazyiter_gen(n=25).max_efficiency_polygon()
    print(max_efficiency_polygon)
    end = time.time()
    print("end time:", end)
    print("time taken:", end - start)

    print("********* using generator as lazy iterator using iter and next")
    start = time.time()
    print("start time:", start)
    max_efficiency_polygon = Polygon_lazyiter_next(n=25).max_efficiency_polygon()
    print(max_efficiency_polygon)
    end = time.time()
    print("end time:", end)
    print("time taken:", end - start)

if __name__ == '__main__':
    test_polygon() 
