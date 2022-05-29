from game.casting.actor import Actor
from game.casting.menu import Menu
from game.shared.point import Point
from game.shared.functions import Functions
from constants import *


class HUD:
    """
    The Heads-Up-Display for battles.
    
    The responsibility of HUD is to keep track of the display of the HUD,
    and make necessary changes when prompted to do so.
    
    Attributes:
        menu (Menu): the menu of options
        selection (integer): the selected option's index
        left (list): the list of Actors for the left menu
        middle (list): the list of Actors for the middle menu
        right (list): the list of Actors for the right menu
        status (integer): the status of the battle, used for skipping the
        battle info when it is diplayed.
            0 = no info, 1 = first info, 2 = second info
        info (string): the battle information to be displayed
    """

    def __init__(self):
        """
        Constructs a new HUD
        """
        self._menu = Menu()
        self._selection = 0
        self._left = []
        self._middle = []
        self._right = []
        self._status = 0
        self._info = ''
        self._setup()

    def _setup(self):
        """
        Initial setup for HUD, adding all the necessary actors.
        """
        # setup the left menu
        left_3rd = int(UI_LINE / 3)
        option1 = Actor(position=Point(left_3rd, UI_TOP + UI_SPACE))
        option2 = Actor(position=Point(left_3rd, UI_TOP + FONT_SIZE + 2 * UI_SPACE))
        option3 = Actor(position=Point(left_3rd, UI_TOP + 2 * FONT_SIZE + 3 * UI_SPACE))
        cursor = Actor('>', position=Point(int(left_3rd / 2), UI_TOP + UI_SPACE))

        self._left.append(option1)
        self._left.append(option2)
        self._left.append(option3)
        self._left.append(cursor)

        # setup the middle menu
        info_font_size = int(FONT_SIZE * 0.75)
        line1 = Actor(font_size=info_font_size, centered=True)
        line2 = Actor(font_size=info_font_size, centered=True)

        self._middle.append(line1)
        self._middle.append(line2)

        # setup the right menu
        y_offset = int(FONT_SIZE / 2)
        hp = Actor(position=Point(int(UI_LINE * 3 + FONT_SIZE), int(UI_MIDDLE-y_offset)))

        self._right.append(hp)

    def reset(self):
        """
        Resets the status value.
        """
        self._status = 0

    def _left_menu(self):
        """
        Updates information in the left menu
        """
        self._update_cursor(self._left[3])
        op1 = self._left[0]
        op2 = self._left[1]
        op3 = self._left[2]
        options = self._menu.get_menu_options()

        op1.set_text(options[0])
        op2.set_text(options[1])
        op3.set_text(options[2])

    def _middle_menu(self, player=None):
        """
        Updates information in the middle menu. Will display the current
        selection's information text if a player is given. Otherwise, will
        display the internal info value.

        Args:
            player (BattleActor): the player
        """
        info = self._info
        # if a player is given, do this
        if player is not None and self._status == 0:
            info = player.get_info(self._menu.get_parent_option(), self._selection)

        # if the current status is to display the first text, do this
        if self._status == 1:
            info = self._info[0]
        elif self._status == 2:
            info = self._info[1]

        info_font_size = self._middle[0].get_font_size()
        width = Functions.measure_text(info, info_font_size)
        max_width = MAX_X - (UI_LINE * 2 + info_font_size * 2)
        ui_offset = int(UI_MIDDLE - info_font_size/2)

        if width > max_width:
            new_list = Functions.split_string(info, info_font_size, max_width)
            self._middle[0].set_text(new_list[0])
            self._middle[1].set_text(new_list[1])

            self._middle[0].set_position(Point(X_MIDDLE, ui_offset - info_font_size))
            self._middle[1].set_position(Point(X_MIDDLE, ui_offset + info_font_size))
        else:
            self._middle[0].set_text(info)
            self._middle[1].set_text('')

            self._middle[0].set_position(Point(X_MIDDLE, ui_offset))

    def _right_menu(self, player):
        """
        Updates information in the right menu
        """
        hp = player.get_health()
        total = player.get_total_health()

        self._right[0].set_text(f'Health: {hp}/{total}')

    def change_menu(self, key, cast):
        """
        Advances the current menu based on the current selection. Skips
        battle information, updates the currently displayed info, and
        moves cursor to another item.

        Args:
            key (string): the key being pressed
            cast (Collection): the cast
        """
        player = cast.get_first_item('player')
        enemy = cast.get_first_item('enemies').get_current()
        screen = cast.get_items('ui')[1]
        if self._status != 0:
            if self._status == 1 and key == 'enter':
                self._status = 2
            elif self._status == 2 and key == 'enter':
                self._status = 0
                if enemy.get_health() == 0:
                    screen.set_state('reward', cast)
            return

        if key is None or (self._selection == self._menu.get_max_selection() and key == 'down'):
            pass
        elif self._selection == 0 and key == 'up':
            pass
        elif key != 'enter':
            if key == 'up':
                self._selection -= 1
            elif key == 'down':
                self._selection += 1
        else:
            self._menu.change_to(self._selection)
            if isinstance(self._menu.get_menu_options(), str):
                player.set_action([self._menu.get_parent_option(), self._selection])
                screen.should_take_turn(True)
                self._status = 1
                self._menu.reset_menu()
                self._left_menu()

    def update_HUD(self, info, player):
        """
        Updates the HUD in each menu with the given variables

        Args:
            info (string, list): the information string, or list of strings
            player (Player): the player
        """
        if self._status != 0:
            if info != self._info and isinstance(info, list):
                self._info = info
        elif self._status == 0:
            if info != self._info:
                self._info = info

        # if there is no battle update text to be displayed, do this
        if self._status == 0:
            # selected option
            sel_op = self._menu.get_menu_options()[self._selection]
            self._left_menu()
            self._right_menu(player)

            # if the option selected is not back, do this
            if sel_op != 'Back':
                # if the options are not the first options, do this
                if sel_op not in ['Attack', 'Defend', 'Magic']:
                    self._middle_menu(player)
                # otherwise, do this
                else:
                    self._middle_menu()
            # otherwise, do this
            else:
                self._middle_menu()

        # if the first info text needs to be displayed, do this
        elif self._status == 1:
            self._right_menu(player)
            self._middle_menu()
        else:
            self._right_menu(player)
            self._middle_menu()

    def get_hud(self):
        """
        Returns all of the HUD text as a list of Actors

        Returns:
            list: the list of all actors making up the HUD
        """
        return Functions.make_flat_list([self._left, self._middle, self._right])

    def set_info(self, given):
        """
        Sets the information text to the given value

        Args:
            given (string): sets the information text to the given value
        """
        self._info = given

    def _update_cursor(self, cursor):
        """
        Updates the cursor in regards to the currently selected menu option.
        
        Args:
            cursor (Actor): the actor representing the cursor
        """
        select = self._selection
        x = cursor.get_position().get_x()

        op1_y = self._left[0].get_position().get_y()
        op2_y = self._left[1].get_position().get_y()
        op3_y = self._left[2].get_position().get_y()

        if select == 0:
            cursor.set_position(Point(x, op1_y))
        if select == 1:
            cursor.set_position(Point(x, op2_y))
        if select == 2:
            cursor.set_position(Point(x, op3_y))
