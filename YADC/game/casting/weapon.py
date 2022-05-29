from random import randint


class Weapon:
    """
    A weapon, to be used by the player.
    
    The responsibility of Weapon is to keep track of relevant information,
    reduce enemy hp, or set player's damage reduction when called to do
    so.
    
    Attributes:
        info (Dict): the dictionary of information text strings
        updates (Dict): the dictionary of battle update text strings
    """

    def __init__(self):
        self._info = {
            'Attack': ['Deals damage to the enemy',
                        'Deals double damage 33% of the time, otherwise deals half damage'],
            'Defend': ['Blocks an incoming attack',
                        'Blocks 50% of an incoming attack, strikes back for 50% damage']
        }
        self._updates = {
            'Attack': ['You give the enemy a beating',
                        'You stabbed the enemy'],
            'Defend': [['You get ready to block an attack', 'The enemy swings, but only makes contact with your sword'],
                        'You react to the enemy\'s movements, but leave yourself open to an attack']
        }

    def get_info(self):
        """
        Returns the Attack and Defend information texts
        
        Returns:
            Dict: the information texts of this weapon's moves
        """
        return self._info

    def get_updates(self):
        """
        Returns the updates information texts
        
        Returns:
            Dict: the information texts of this weapon's """
        return self._updates

    def attack1(self, enemy, damage):
        """
        Deals damage to the enemy.
        
        Args:
            enemy (BattleActor): the targeted enemy
            damage (integer): the damage value
        """
        dr = enemy.get_damage_reduction()
        hp = enemy.get_health()

        enemy.set_health(self._reduce_hp(damage, dr, hp))
    
    def attack2(self, enemy, damage):
        """
        Deals damage to the enemy. 1 in 3 chance of crit for double
        damage, otherwise half damage.
        
        Args:
            enemy (BattleActor): the targeted enemy
            damage (integer): the damage value
        """
        dr = enemy.get_damage_reduction()
        hp = enemy.get_health()

        number = randint(1, 3)
        if number == 1:
            damage *= 2
        else:
            damage /= 2

        enemy.set_health(self._reduce_hp(damage, dr, hp))

    def defend1(self, player, enemy):
        """
        Defends against an incoming attack.
        
        Args:
            player (BattleActor): the player BattleActor
            enemy (BattleActor): the targeted enemy
        """
        player.set_damage_reduction(100)

    def defend2(self, player, enemy):
        """
        Defends against an incoming attack. Deals a percentage of the
        player's damage stat back to the enemy, if they attack.
        
        Args:
            player (BattleActor): the player BattleActor
            enemy (BattleActor): the targeted enemy
        """
        player.set_damage_reduction(50)

        damage = player.get_damage() * 1/2
        dr = enemy.get_damage_reduction()
        hp = enemy.get_health()

        enemy.set_health(self._reduce_hp(damage, dr, hp))

    def _reduce_hp(self, damage, dr, hp):
        """
        Reduces the enemy's hp based on the given values. Will not go
        below zero.
        
        Args:
            damage (integer): the damage value of the attack
            dr (integer): the enemy's percentage damage reduction
            hp (integer): the enemy's current hp
            
        Returns:
            integer: the new, lowered hp value
        """
        new_hp = int(hp - damage * (1 - dr/100))
        if new_hp < 0:
            new_hp = 0

        return new_hp
