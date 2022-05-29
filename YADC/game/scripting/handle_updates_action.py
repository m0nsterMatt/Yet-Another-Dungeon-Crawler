from game.scripting.action import Action
from random import randint


class HandleUpdatesAction(Action):
    """
    An update Action that updates various values across the game.
    
    The responsibility of HandleUpdatesAction is to handle all the
    necessary updates, including screen change and taking a turn
    """
    def __init__(self):
        """
        Constructs a new HandleUpdatesAction.
        """
        super().__init__()

    def execute(self, cast, script):
        """
        Executes the Handle Updates Action.
        
        Args:
            cast (Cast): the cast of Actors in the game
            script (Script): the script of actions in the game
        """
        player = cast.get_first_item('player')
        enemy = cast.get_first_item('enemies').get_current()
        ui = cast.get_items('ui')
        hud = ui[0]
        screen = ui[1]

        if enemy is None:
            screen.set_state('end', cast)

        if screen.get_state() == 'battle':
            info_text = enemy.get_info()
            if screen.should_take_turn():
                info_text = self._battle_updates(cast, screen)
            if screen.get_state() == 'battle':
                hud.update_HUD(info_text, player)

    def _battle_updates(self, cast, screen):
        """
        Handles all the necessary battle updates.
        
        Args:
            cast (Collection): the cast
            screen (Screen): the current display
        """
        enemy = cast.get_first_item('enemies').get_current()
        player = cast.get_first_item('player')

        player_action = player.get_action()[0]
        player_action_index = player.get_action()[1]
        
        # information text list
        info_list = []
        # do the textual representation of these updates
        player_info = player.get_updates(player_action, player_action_index)
        enemy_info = 'The enemy attacked, dealing damage'

        # do the combat updates
        if player_action == 'Defend' and player_action_index == 0:
            player.defend(enemy)

        if player_action == 'Attack':
            player.attack(enemy)
        elif player_action == 'Defend' and player_action_index == 1:
            player.defend(enemy)
        elif player_action == 'Magic':
            player.magic()

        if enemy.get_health() != 0:
            enemy.attack(player)
        else:
            enemy_info = 'The enemy has died!'

        # reset the damage reduction of both BattleActors
        enemy.set_damage_reduction(0)
        player.set_damage_reduction(0)

        # if the player chose to defend...
        if player_action == 'Defend':
            # and the player chose to block...
            if player_action_index == 0:
                info_list.append(player_info[0])
                info_list.append(player_info[1])
            # and the player chose to parry...
            elif player_action_index == 1:
                info_list.append(player_info)
                info_list.append(enemy_info)
        # if the player chose to attack...
        elif player_action == 'Attack':
            info_list.append(player_info)
            info_list.append(enemy_info)
        # if the player chose to heal...
        elif player_action == 'Magic':
            info_list.append(player_info)
            info_list.append(enemy_info)

        # stop another turn from being taken
        if player.get_health() == 0:
            screen.set_state('end', cast)
        screen.should_take_turn(False)
        return info_list
