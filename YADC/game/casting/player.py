from game.casting.battle_actor import BattleActor
from game.casting.weapon import Weapon
from math import ceil

class Player(BattleActor):
    """
    The player character.

    The responsibility of Player is to keep track of and change values
    relevant to the player, including both player stats, and reducing
    enemy stats if attacking.

    Attributes:
        action (list): the player's [action, index]
            ex. ['Attack', 0] or ['Magic', 1]
        item (Weapon): the currently held weapon
        item_info (Dict): the dictionary of item information text strings
        item_updates (Dict): the dictionary of battle update text strings
    """

    def __init__(self):
        """
        Constructs a new Player.
        """
        super().__init__('player', 100, 10, '')
        self._action = []
        self._item = Weapon()
        self._item_info = self._item.get_info()
        self._item_info['Magic'] = ['Heal 25% total health',
                                    'Set health to 40%']
        self._item_updates = self._item.get_updates()
        self._item_updates['Magic'] = ['You drink the potion, and feel your wounds closing',
                                        'You feel your body change as a result of the spell']

    def levelup(self):
        """
        Levels up the player by increasing health and damage somewhat.
        Will keep health percentage the same.
        """
        health_percent = self._health / self._total_health
        self._total_health = ceil(self._total_health * 1.10)
        self._damage = ceil(self._damage * 1.10)
        self._health = int(self._total_health * health_percent)

    def reset(self):
        """
        Resets the stats of the player.
        """
        self._health = 100
        self._total_health = 100
        self._damage = 10

    def set_action(self, given):
        """
        Sets the player's action to the given.
        
        Args:
            given (list): the [action, index] to be set to
        """
        if given[0] in ['Attack', 'Defend', 'Magic'] and given[1] in [0, 1]:
            self._action = given

    def get_action(self):
        """
        Gets the player's current action.
        """
        return self._action

    def get_info(self, key, index):
        """
        Returns the player action information depending on key and index
        given.
        
        Args:
            key (string): the key value, one of three values:
                Attack, Defend, Magic
            index (integer): the index of the selected action
        """
        return self._item_info[key][index]

    def get_updates(self, key, index):
        """
        Returns the player battle update information depending on the key
        and index given.
        
        Args:
            key (string): the key value, one of three values:
                Attack, Defend, Magic
            index (integer): the index of the selected action
        """
        return self._item_updates[key][index]

    def attack(self, enemy):
        """
        Attacks the given enemy using the player's current action.
        
        Args:
            enemy (BattleActor): the targeted enemy
        """
        action_index = self._action[1]

        if action_index == 0:
            self._item.attack1(enemy, self._damage)
        else:
            self._item.attack2(enemy, self._damage)

    def defend(self, enemy):
        """
        Defends against an enemy's attacks based on the player's current
        action.
        
        Args:
            enemy (BattleActor): the targeted enemy
        """
        action_index = self._action[1]

        if action_index == 0:
            self._item.defend1(self, enemy)
        if action_index == 1:
            self._item.defend2(self, enemy)

    def magic(self):
        """
        Heals the player based on their current action.
        """
        action_index = self._action[1]
        if action_index == 0:
            new_hp = int(self._total_health * .25)
            if new_hp + self._health > self._total_health:
                new_hp = self._total_health - self._health
            self.set_health(self._health + new_hp)
        else:
            self.set_health(int(self._total_health * .4))
