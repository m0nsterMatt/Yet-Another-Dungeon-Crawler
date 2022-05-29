from game.casting.actor import Actor
from game.casting.battle_actor import BattleActor
from game.shared.color import Color
from game.shared.point import Point


def test_Actor():
    # setup
    a = Actor(centered=True)
    c = Color(1,2,3,4)
    p = Point(6,7)
    v = Point(9,10)

    # test get/set methods
    a.set_color(c)
    a.set_font_size(5)
    a.set_position(p)
    a.set_text(8)
    a.set_velocity(v)
    assert a.is_centered()
    assert a.get_color() == (1,2,3,4)
    assert a.get_font_size() == 5
    assert a.get_position() == p
    assert a.get_text() == 8
    assert a.get_velocity() == v

def test_BattleActor():
    # setup
    b = BattleActor('name', 10, 10, 'info')

    # test the get/set methods
    b.set_damage(20)
    assert b.get_damage() == 20
    b.set_damage_reduction(20)
    assert b.get_damage_reduction() == 20
    b.set_health(20)
    assert b.get_health()
    b.set_name('something')
    assert b.get_name() == 'something'
    b.set_total_health(30)
    assert b.get_total_health() == 30
    assert b.get_info() == 'info'

    # test the copy method
    c = b.copy()
    assert b.get_damage() == c.get_damage()
    assert b.get_total_health() == c.get_health()
    assert b.get_info() == c.get_info()
    assert b.get_name() == c.get_name()
    assert b.get_total_health() == c.get_total_health()

    # test the attack method
    b.set_damage_reduction(0)
    b.set_damage(29)
    b.attack(c)
    assert c.get_health() == 1
    b.attack(c)
    assert c.get_health() == 0
