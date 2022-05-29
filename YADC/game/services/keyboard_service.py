import pyray
from game.shared.point import Point


class KeyboardService:
    """
    Detects player input.
    
    The responsibility of KeyboardService is to indicate whether a key is
    being pressed.
    
    Attributes:
        _keys (Dict[string, int]): the letter to key mapping
    """
    
    def __init__(self):
        """
        Constructs a new KeyboardService
        """
        self._keys = {}

        self._keys['up'] = pyray.KEY_UP
        self._keys['down'] = pyray.KEY_DOWN

        self._keys['enter'] = pyray.KEY_ENTER

    def is_key_pressed(self, key):
        """
        Checks if the given key is being pressed.
        
        Args:
            key (string): the given key
        """
        pyray_key = self._keys[key.lower()]
        return pyray.is_key_pressed(pyray_key)
