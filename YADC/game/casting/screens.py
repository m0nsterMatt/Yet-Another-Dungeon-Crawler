from game.casting.actor import Actor
from game.shared.point import Point
from constants import *

class Screen:
    """
    What is seen by the user.
    
    The responsibility of Screen is to keep track of what is output to the
    game window, and when.
    
    Attributes:
        state (string): the game's current state
        previous_state (string): the game's previous state
        screen (list): a list of Actors to be displayed
        should_take_turn (bool): whether or not a turn should be taken
    """

    def __init__(self):
        """
        Constructs a new Screen.
        """
        self._state = 'title'
        self._previous_state = 'title'
        self._screen = []
        self._should_take_turn = False
        self._title_screen()

    def set_state(self, given, cast):
        """
        Sets the state to the given state, if the given state is in the possible
        states list:
            title, battle, reward, end
        
        Args:
            given (string): a state to be changed to
            cast (Collection): the cast
        """
        if given in ['title', 'battle', 'reward', 'end']:
            self._state = given
            if self._state != self._previous_state and self._state != 'battle':
                self._update_screen(cast)
            self._previous_state = self._state

    def get_state(self):
        """
        Returns the current state out of the following list:
            title, battle, reward, end

        
        Returns:
            string: the current state as a string
        """
        return self._state

    def get_screen(self, cast):
        """
        Gets the current screen as a list of Actors.

        Args:
            cast (Collection): the cast
        """
        if self._state == 'battle':
            self._battle_screen(cast)
        return self._screen

    def _update_screen(self, cast):
        """
        Updates the screen according to the current state.
        """
        self._screen = []
        if self._state == 'title':
            self._title_screen()
        elif self._state == 'reward':
            try:
                self._reward_screen(cast)
            except:
                self._end_screen(cast)
        elif self._state == 'end':
            self._end_screen(cast)

    def should_take_turn(self, given=None):
        """
        If no arguments are passed, returns if a turn should be taken.
        Otherwise, sets should_take_turn to the given value.

        Args:
            given (boolean): whether or not a turn should be taken
        """
        if given is None:
            return self._should_take_turn
        else:
            self._should_take_turn = given

    def _title_screen(self):
        """
        Creates a title screen, and saves it as the current screen.
        """
        text1 = Actor('Yet Another Dungeon Crawler', int(FONT_SIZE * 2), position=Point(X_MIDDLE, int(MAX_Y / 4)), centered=True)
        text2 = Actor('Press ENTER to Start', position=Point(X_MIDDLE, int(MAX_Y / 4 * 3)), centered=True)

        self._screen.append(text1)
        self._screen.append(text2)

    def _battle_screen(self, cast):
        """
        Gets the HUD for a battle, and saves it as the current screen.

        Args:
            cast (Collection): the cast
        """
        self._screen = cast.get_first_item('ui').get_hud()
    
    def _reward_screen(self, cast):
        """
        Creates a reward screen, and saves it as the current screen.
        """
        text1 = Actor('The battle\'s over, for now...', FONT_SIZE * 2, position=Point(X_MIDDLE, int(MAX_Y / 8)), centered=True)
        text2 = Actor('You leveled up!', int(FONT_SIZE * 1.5), position=Point(X_MIDDLE, int(MAX_Y / 5)), centered=True)

        self._screen.append(text1)
        self._screen.append(text2)

        cast.get_first_item('enemies').advance_room()
        cast.get_first_item('player').levelup()
    
    def _end_screen(self, cast):
        """
        Creates an end screen, and saves it as the current screen.

        Args:
            cast (Collection): the cast of Actors
        """
        text1 = Actor(font_size = FONT_SIZE * 2, position=Point(X_MIDDLE, int(MAX_Y / 4)), centered=True)
        if cast.get_first_item('player').get_health() == 0:
            text1.set_text('Another Skeleton now Lies in the Halls...')
        else:
            text1.set_text('You Escaped the Dungeon!')

        text2 = Actor('Press ENTER to Play Again', position=Point(X_MIDDLE, int(MAX_Y / 4 * 3)), centered=True)

        self._screen.append(text1)
        self._screen.append(text2)

        cast.get_first_item('enemies').prepare()
        cast.get_first_item('player').reset()
        cast.get_first_item('ui').reset()
