from game.casting.battle_actor import BattleActor
from random import choice

class Rooms():
    """
    A set of rooms for the player to go through.
    
    The responsibility of Rooms is to hold a collection of rooms, randomly
    pick from them to create a full game progression, and to keep track of
    that progression.
    
    Attributes:
        battles (list): the possible enemies the player can face
        bosses (list): the possible bosses the player can face
        final_rooms (list): the final set of rooms to be used
        current (BattleActor): the current enemy being faced
    """

    def __init__(self):
        """
        Constructs a new Rooms.
        """
        self._battles = [
            BattleActor('Human', 10, 10, 'A human, gone mad from the endless halls, stands before you'),
            BattleActor('Goblin', 6, 6, 'A goblin crawls out of the shadows'),
            BattleActor('Warrior', 10, 15, 'A warrior blocks your path.'),
            BattleActor('Knight', 15, 10, 'A knight forbids you from passing'),
            BattleActor('Wizard', 5, 20, 'A wizard cackles at you'),
            BattleActor('Wolf', 7, 9, 'A wolf growls at you'),
            BattleActor('Spider', 3, 20, 'A massive spider crawls towards you'),
            BattleActor('Flesh Wall', 15, 3, 'A wall of flesh blocks your way'),
            BattleActor('Evil Egg', 5, 10, 'An egg, full of hatred, blocks your path'),
            BattleActor('Rat', 5, 5, 'A dog-sized rat rushes towards you'),
            BattleActor('Snake', 5, 12, 'A giant snake slithers menacingly before you'),
            BattleActor('Lost Spirit', 10, 7, 'A lost spirit floats in front of you'),
            BattleActor('Poison Mushroom', 10, 3, 'A giant mushroom emits toxic clouds, blocking your way'),
            BattleActor('Skeleton', 7, 5, 'A skeleton rattles his bones spookily'),
            BattleActor('Haunted Sword', 4, 10, 'A sword eerily floats in front of you'),
            BattleActor('Arm mass', 8, 14, 'A giant mass of arms wriggles before you'),
            BattleActor('Puppy', 50, 1, 'A rat-sized dog scampers towards you')
        ]
        self._bosses = [
            BattleActor('Giant Tree', 20, 20, 'A massive, evil tree blocks the exit'),
            BattleActor('Master Ninja', 10, 30, 'You see the exit, but a master ninja stops you from proceeding'),
            BattleActor('Dark Knight', 28, 12, 'A dark knight stands between you and the exit'),
            BattleActor('Void', 30, 10, 'An endless abyss lies between you and the exit'),
            BattleActor('Jailer', 25, 15, 'The dungeon jailer locks the exit door, and readies his whip')
        ]
        self._final_rooms = []
        self._current = None
        self.prepare()

    def prepare(self, number=10):
        """
        Prepares the final rooms list by selecting randomly from the
        possible rooms.
        
        Args:
            number (integer): the number of rooms to be selected
        """
        multiplier = .75
        self._final_rooms = []
        for i in range(number - 1):
            chosen = 'battle'

            if chosen == 'battle':
                room = choice(self._battles).copy()
                room.set_health(int(room.get_health() * 4 * multiplier))
                room.set_total_health(int(room.get_total_health() * 4 * multiplier))
                room.set_damage(int(room.get_damage() * multiplier))

            self._final_rooms.append(room)
            multiplier *= 1.11

        boss = choice(self._bosses).copy()
        boss.set_health(int(boss.get_health() * 5 * multiplier))
        boss.set_total_health(int(boss.get_total_health() * 5 * multiplier))
        boss.set_damage(int(boss.get_damage() * multiplier))
        self._final_rooms.append(boss)
        self._current = self._final_rooms.pop(0)
    
    def get_rooms(self):
        """
        Returns the final rooms list.
        
        Returns:
            list: the final rooms list"""
        return self._final_rooms
    
    def get_current(self):
        """
        Returns the current room if one is present. Otherwise, returns
        None.
        
        Returns:
            BattleActor (or None): the current room
        """
        return self._current

    def advance_room(self):
        """
        Advances the current room to the next room, and removes the
        previous room from the final rooms list.
        """
        try:
            self._current = self._final_rooms.pop(0)
        except IndexError:
            self._current = None
