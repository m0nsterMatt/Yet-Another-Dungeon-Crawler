from constants import *
from game.scripting.action import Action


class ControlActorsAction(Action):
    """
    An input action that controls menu changes.
    
    The responsibility of ControlActorsAction is to get the pressed key
    and pass it to the HUD for updates.
    
    Attributes:
        _keyboard_service (KeyboardService): an instance of KeyboardService
    """

    def __init__(self, keyboard_service):
        """
        Constructs a new ControlActorsAction using the specified
        KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): an instance of
                KeyboardService
        """
        self._keyboard_service = keyboard_service

    def execute(self, cast, script):
        """
        Executes the Control Actors Action.
        
        Args:
            cast (Cast): the cast of Actors in the game
            script (Script): the script of actions in the game
        """
        player = cast.get_first_item('player')
        enemy = cast.get_first_item('enemies').get_current()
        ui = cast.get_items('ui')
        hud = ui[0]
        screen = ui[1]
        state = screen.get_state()


        u, d, enter = False, False, False

        if self._keyboard_service.is_key_pressed('up'):
            u = True

        if self._keyboard_service.is_key_pressed('down'):
            d = True

        if self._keyboard_service.is_key_pressed('enter'):
            enter = True


        if state != 'battle' and enter:
            if state != 'end':
                screen.set_state('battle', cast)
            else:
                screen.set_state('title', cast)

        else:
            if u:
                key = 'up'
            elif d:
                key = 'down'
            elif enter:
                key = 'enter'
            else:
                key = None

            hud.change_menu(key, cast)