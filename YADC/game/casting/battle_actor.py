class BattleActor():
    """
    A thing taking part in a battle.
    
    The responsibility of BattleActor is to keep track of its own various
    stats, to attack, reducing the target's health, and to defend, setting
    its own damage reduction to 100
    
    Attributes:
        name (string): the name
        health (integer): the current health
        damage (integer): the damage value
        information (string): the information text
        total_health (integer): the max health
        damage_reduction (integer): the percentage of damage reduction
    """

    def __init__(self, name, health, damage, info):
        """
        Constructs a new BattleActor using the given values

        Args:
            name (string): the name of the BattleActor
            health (integer): the max health of the BattleActor
            damage (integer): the damage value of the BattleActor
            info (string): the information text of the BattleActor
        """
        self._name = name
        self._health = health
        self._damage = damage
        self._information = info
        self._total_health = health
        self._damage_reduction = 0

    def copy(self):
        """
        Returns a copy of itself
        
        Returns:
            BattleActor: an exact duplicate of itself
        """
        return BattleActor(self._name, self._total_health, self._damage, self._information)

    def get_name(self):
        """
        Gets the name of the BattleActor.

        Returns:
            string: the name of the BattleActor
        """
        return self._name

    def get_health(self):
        """
        Gets the health of the BattleActor.

        Returns:
            integer: the current health value
        """
        return self._health

    def get_total_health(self):
        """
        Gets the total health of the BattleActor.

        Returns:
            integer: the total health value
        """
        return self._total_health

    def get_damage(self):
        """
        Gets the damage of the BattleActor.

        Returns:
            integer: the damage value
        """
        return self._damage

    def get_damage_reduction(self):
        """
        Gets the damage reduction percentage of the BattleActor.

        Returns:
            integer: the damage reduction percentage
        """
        return self._damage_reduction

    def get_info(self):
        """
        Gets the information text of the BattleActor.

        Returns:
            string: the information text
        """
        return self._information

    def set_name(self, given):
        """
        Sets the name of the BattleActor to the given value.
        
        Args:
            given (string): the given value
        """
        self._name = given

    def set_health(self, given):
        """
        Sets the health of the BattleActor to the given value.
        
        Args:
            given (integer): the given value
        """
        self._health = given

    def set_total_health(self, given):
        """
        Sets the total health of the BattleActor to the given value.
        
        Args:
            given (integer): the given value
        """
        self._total_health = given

    def set_damage(self, given):
        """
        Sets the damage of the BattleActor to the given value.
        
        Args:
            given (integer): the given value
        """
        self._damage = given

    def set_damage_reduction(self, given):
        """
        Sets the damage reduction of the BattleActor to the given value.
        
        Args:
            given (integer): the given value
        """
        self._damage_reduction = given

    def attack(self, enemy):
        """
        Attacks the opponent, lowering their health.
        
        Args:
            enemy (BattleActor): the opponent being targeted
        """
        dr = enemy.get_damage_reduction()
        hp = enemy.get_health()

        new_hp = int(hp - self._damage * (1 - dr/100))
        if new_hp < 0:
            new_hp = 0

        enemy.set_health(new_hp)
