class Color:
    """
    A color.
    
    The responsibility of Color is to hold and provide information about
    itself. Color has a convenience method for converting it to a tuple.
    
    Attributes:
        _red (int):     the red value
        _green (int):   the green value
        _blue (int):    the blue value
        _alpha (int):   the alpha value
    """

    def __init__(self, red, green, blue, alpha = 255):
        """
        Constructs a new Color, using the given values.

        Args:
            red (int):      the red value
            green (int):    the green value
            blue (int):     the blue value
            alpha (int):    the alpha value
        """
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def to_tuple(self):
        """
        Returns the color as a tuple of four values (red, green, blue,
        alpha).

        Returns:
            Tuple(int, int, int, int): the color as a tuple
        """
        return (self._red, self._green, self._blue, self._alpha)
