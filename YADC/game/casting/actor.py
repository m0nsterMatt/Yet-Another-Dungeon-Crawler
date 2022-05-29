from constants import *
from game.shared.point import Point

class Actor:
    """
    A visible, movable thing that participates in the game.
    
    The responsibility of Actor is to keep track of its own appearance,
    position, and velocity in 2D space.
    
    Attributes:
        _text (string):     the text to display
        _font_size (int):   the font size to use
        _color (Color):     the color of the text
        _position (Point):  the screen coordinates
        _velocity (Point):  the speed and direction
    """

    def __init__(self, text='', font_size=FONT_SIZE, color=WHITE, \
        position=Point(0,0), velocity=Point(0,0), centered=False):
        """
        Constructs a new Actor.
        """
        self._text = text
        self._font_size = font_size
        self._color = color
        self._position = position
        self._velocity = velocity
        self._centered = centered

    def get_text(self):
        """
        Gets the Actor's textual representation.
        
        Returns
            string: the Actor's textual representation
        """
        return self._text

    def get_font_size(self):
        """
        Gets the Actor's font size.
        
        Returns
            string: the Actor's font size
        """
        return self._font_size

    def get_color(self):
        """
        Gets the Actor's color as a tuple.
        
        Returns
            tuple(int, int, int, int): the Actor's color
        """
        return self._color.to_tuple()

    def get_position(self):
        """
        Gets the Actor's x,y position.
        
        Returns
            string: the Actor's x,y position
        """
        return self._position

    def get_velocity(self):
        """
        Gets the Actor's speed and direction.
        
        Returns
            string: the Actor's velocity
        """
        return self._velocity

    def move_next(self):
        """
        Moves the Actor to its next position according to its velocity.
        Will not move when reaching maximum x or y values
        """
        x = (self._position.get_x() + self._velocity.get_x())
        y = (self._position.get_y() + self._velocity.get_y())

        if x >= MAX_X or y >= MAX_Y:
            return

        self._position = Point(x, y)

    def is_centered(self):
        """
        Returns whether the text should be centered when drawn.
        
        Returns:
            boolean: whether the text should be centered
        """
        return self._centered

    def set_text(self, given):
        """
        Updates the Actor's text to the given value.
        
        Args:
            given (string): the given text
        """
        self._text = given

    def set_font_size(self, given):
        """
        Updates the Actor's font size to the given value.
        
        Args:
            given (int): the given font size
        """
        self._font_size = given

    def set_color(self, given):
        """
        Updates the Actor's color to the given value.
        
        Args:
            given (Color): the given color
        """
        self._color = given

    def set_position(self, given):
        """
        Updates the Actor's position to the given value.
        
        Args:
            given (Point): the given position
        """
        self._position = given

    def set_velocity(self, given):
        """
        Updates the Actor's velocity to the given value.
        
        Args:
            given (Point): the given velocity
        """
        self._velocity = given
