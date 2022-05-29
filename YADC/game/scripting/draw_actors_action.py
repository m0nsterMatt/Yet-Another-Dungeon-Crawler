from game.scripting.action import Action
from pyray import draw_line, draw_rectangle
from constants import *


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.
    
    Attributes:
        _video_service (VideoService): an instance of VideoService
    """

    def __init__(self, video_service):
        """
        Constructs a new DrawActorsAction using the specified
        VideoService.
        
        Args:
            video_service (VideoService): an instance of VideoService
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """
        Executes the Draw Actors Action.
        
        Args:
            cast (Cast): the cast of Actors in the game
            script (Script): the script of Actions in the game
        """
        screen_class = cast.get_items('ui')[1]
        state = screen_class.get_state()
        screen = screen_class.get_screen(cast)

        self._video_service.clear_buffer()
        if state == 'battle':
            self._draw_ui()
            self._draw_health_bar(cast)
        self._video_service.draw_actors(screen)
        self._video_service.flush_buffer()

    def _draw_ui(self):
        """
        Draw the lines for the UI
        """
        draw_line(0, UI_TOP, MAX_X, UI_TOP, WHITE.to_tuple())
        draw_line(UI_LINE, MAX_Y, UI_LINE, UI_TOP, WHITE.to_tuple())
        draw_line(UI_LINE * 3, MAX_Y, UI_LINE * 3, UI_TOP, WHITE.to_tuple())

    def _draw_health_bar(self, cast):
        """
        Draw the health bar for the enemy
        """
        enemy = cast.get_first_item('enemies').get_current()
        total = enemy.get_total_health()
        current = enemy.get_health()

        percent_total = current / total

        corner_x = UI_LINE / 2
        total_width = MAX_X - UI_LINE
        corner_y = int(MAX_Y / 8)

        r1x = int(corner_x)
        r1y = corner_y
        r1w = int(total_width * percent_total)
        r1h = FONT_SIZE

        r2x = r1x + r1w
        r2y = corner_y
        r2w = int(total_width * (1 - percent_total))
        r2h = FONT_SIZE

        # draw the health bar of the enemy
        draw_rectangle(r1x, r1y, r1w, r1h, GREEN.to_tuple())
        draw_rectangle(r2x, r2y, r2w, r2h, RED.to_tuple())
