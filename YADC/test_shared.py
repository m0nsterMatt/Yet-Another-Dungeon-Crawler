from game.shared.collection import Collection
from game.shared.color import Color
from game.shared.functions import Functions
from game.shared.point import Point
from game.casting.actor import Actor

def test_Collection():
    # setup
    a1 = Actor()
    a2 = Actor()
    a3 = Actor()
    c = Collection()

    # test add_item method
    c.add_item('one', a1)
    c.add_item('one', a2)
    c.add_item('two', a3)

    # test get_items... methods
    assert c.get_items('one') == [a1, a2]
    assert c.get_items('two') == [a3]
    assert c.get_all_items() == [a1, a2, a3]
    assert c.get_first_item('one') == a1
    assert c.get_first_item('two') == a3

    # test remove_item method
    c.remove_item('one', a2)
    assert c.get_items('one') == [a1]
    c.remove_item('one', a1)
    assert c.get_items('one') == []

    # test remove_group method
    c.remove_group('one')
    assert c.get_all_items() == [a3]
    c.remove_group('two')
    assert c.get_all_items() == []

def test_Color():
    # setup
    c = Color(1,2,3,4)

    # test color attributes and methods
    assert c._red == 1
    assert c._green == 2
    assert c._blue == 3
    assert c._alpha == 4
    assert c.to_tuple() == (1,2,3,4)

    c = Color(9, 10, 11, 12)
    assert c._red == 9
    assert c._green == 10
    assert c._blue == 11
    assert c._alpha == 12
    assert c.to_tuple() == (9,10,11,12)

def test_Functions():
    # test make flat list
    list1 = [1, [[3, [[[1], 2], 9]], 80], 2]
    assert Functions.make_flat_list(list1) == [1, 3, 1, 2, 9, 80, 2]

    list2 = [[[[[[[[[[[[[[4]]]]]]]]]]]]]]
    assert Functions.make_flat_list(list2) == [4]

    list3 = [1,3,2]
    assert Functions.make_flat_list(list3) == [1, 3, 2]

def test_Point():
    # setup
    p1 = Point(1,2)
    p2 = Point(1,2)
    p3 = Point(3,4)

    # test get methods
    assert p1.get_x() == 1
    assert p1.get_y() == 2
    assert p2.get_x() == 1
    assert p2.get_y() == 2
    assert p3.get_x() == 3
    assert p3.get_y() == 4

    # test equals method
    assert p1.equals(p2)
    assert not p1.equals(p3)

    # test add method
    temp = p1.add(p2)
    assert [temp.get_x(), temp.get_y()] == [2, 4]
    temp = p1.add(p3)
    assert [temp.get_x(), temp.get_y()] == [4, 6]

    # test scale method
    temp = p1.scale(5)
    assert [temp.get_x(), temp.get_y()] == [5, 10]
    temp = p1.scale(10)
    assert [temp.get_x(), temp.get_y()] == [10, 20]
    temp = p3.scale(7)
    assert [temp.get_x(), temp.get_y()] == [21, 28]
    temp = p3.scale(19)
    assert [temp.get_x(), temp.get_y()] == [57, 76]
