import pyray
from constants import *


class VideoService:
    """
    Outputs the game state.

    The responsibility of VideoService is to draw the game state onto the
    screen.
    """

    def __init__(self, debug = False):
        """
        Constructs a new VideoService using the given debug mode
        
        Args:
            debug (bool): whether or not to draw in debug mode
        """
        self._debug = debug

    def close_window(self):
        """
        Closes the window and releases all computing resources.
        """
        pyray.close_window()

    def clear_buffer(self):
        """
        Clears the buffer in preparation for the next rendering. This
        method should be called in the beginning of the game's output
        phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug:
            self._draw_grid()

    def draw_actor(self, actor):
        """
        Draws the given Actor's text onto the screen.
        
        Args:
            actor (Actor): the actor to draw
        """
        text = actor.get_text()
        size = actor.get_font_size()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        color = actor.get_color()

        if actor.is_centered():
            x -= self._get_x_offset(text, size)

        pyray.draw_text(text, x, y, size, color)

    def draw_actors(self, actors):
        """
        Draws the text for the given list of actors on the screen.
        
        Args:
            actors (list): the list of actors to draw
        """
        for actor in actors:
            self.draw_actor(actor)

    def flush_buffer(self):
        """
        Copies the buffer contents to the screen. This method should be
        called at the end of the game's output phase.
        """
        pyray.end_drawing()

    def is_window_open(self):
        """
        Whether or not the window was closed.
        
        Returns:
            bool: True if the window is open, false otherwise
        """
        return not pyray.window_should_close()

    def open_window(self):
        """
        Opens a new window with the provided title.
        """
        pyray.init_window(MAX_X, MAX_Y, CAPTION)
        pyray.set_target_fps(FRAME_RATE)

    def _draw_grid(self):
        """
        Draws a grid on the screen.
        """
        for y in range(0, MAX_Y, CELL_SIZE):
            pyray.draw_line(0, y, MAX_X, y, pyray.GRAY)

        for x in range(0, MAX_X, CELL_SIZE):
            pyray.draw_line(x, 0, x, MAX_Y, pyray.GRAY)

    def _get_x_offset(self, text, size):
        """
        Gets the x value offset based on the width of the text

        Args:
            text (string): the text to be measured
        """
        width = pyray.measure_text(text, size)
        return int(width / 2)
