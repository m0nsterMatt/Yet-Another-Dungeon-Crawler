class Point:
    """
    A distance from an origin (0,0).
    
    The responsibility of Point is to hold and provide information about
    itself. Point has convenience methods for adding, scaling, and
    comparing them.

    Attributes:
        _x (int): the distance on the x-axis from the origin
        _y (int): the distance on the y-axis from the origin
    """

    def __init__(self, x, y):
        """
        Constructs a new Point using the given values.
        
        Args:
            x (int): the x value
            y (int): the y value
        """
        self._x = x
        self._y = y

    def add(self, other):
        """
        Returns a new point, which is the sum of this and the given one.

        Args:
            other (Point): the Point to add

        Returns:
            Point: a new Point, which is the sum
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)

    def equals(self, other):
        """
        Whether or not this point and the other one are equal.

        Args:
            other (Point): the Point to compare

        Returns:
            boolean: True if x and y values are equal; False otherwise
        """
        return self._x == other.get_x() and self._y == other.get_y()

    def get_x(self):
        """
        Gets the x value.
        
        Returns:
            integer: the x value
        """
        return self._x

    def get_y(self):
        """
        Gets the y value.
        
        Returns:
            integer: the y value
        """
        return self._y

    def scale(self, factor):
        """
        Scales the point by the given factor.
        
        Args:
            factor (int): the scale factor
        
        Returns:
            Point: a new, scaled Point
        """
        return Point(self._x * factor, self._y * factor)
