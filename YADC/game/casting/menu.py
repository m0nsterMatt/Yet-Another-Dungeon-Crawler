class Menu():
    """
    A menu of options.
    
    The responsibility of Menu is to keep track of the levels of options,
    the currently available options, and the parent options.
    
    Attributes:
        select_menu (Dict): the entire menu
        current_menu (list): the current menu display
        parent_option (string): the parent option
    """
    def __init__(self):
        """
        Constructs a new Menu.
        """
        self._select_menu = {'Attack': ['Wallop', 'Stab', 'Back'], \
                                'Defend': ['Block', 'Parry', 'Back'], \
                                'Magic': ['Potion', 'Spell', 'Back']}
        self._current_menu = list(self._select_menu.keys())
        self._parent_option = ''
        
    def change_to(self, selection):
        """
        Changes the displayed menu according to the selected option. If
        the option chosen is the end of the menu, then sets the current
        menu to that option.
        
        Args:
            selection (integer): the index of the selected option
        """
        list_of_keys = list(self._select_menu.keys())
        if list_of_keys == self._current_menu:
            self._current_menu = self._select_menu[list_of_keys[selection]]
            self._parent_option = list_of_keys[selection]
        else:
            self._current_menu = self._current_menu[selection]
        if self._current_menu == 'Back':
            self._current_menu = list_of_keys

    def get_menu_options(self):
        """
        Returns the possible menu options.
        
        Returns:
            list: the possible menu options
        """
        return self._current_menu

    def get_max_selection(self):
        """
        Returns the maximum selection possible in the current menu.
        
        Returns:
            integer: the maximum index available for selection
        """
        return len(self._current_menu) - 1

    def reset_menu(self):
        """
        Resets the menu to the original values.
        """
        self._current_menu = list(self._select_menu.keys())

    def get_parent_option(self):
        """
        Returns the parent option.
        
        Returns:
            string: the parent option
        """
        return self._parent_option
