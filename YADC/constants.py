from game.shared.color import Color

MAX_X = 1600
X_MIDDLE = int(MAX_X / 2)

MAX_Y = 900
Y_MIDDLE = int(MAX_Y / 2)

UI_LINE = int(MAX_X / 4)
UI_TOP = int(MAX_Y * 5/6)
UI_SPACE = int(UI_TOP / 5 / 10)
UI_MIDDLE = int(UI_TOP + (MAX_Y - UI_TOP) / 2)

COLUMNS = int(MAX_X / 10)
ROWS = int(MAX_Y / 10)
CELL_SIZE = 10


FRAME_RATE = 24
FONT_SIZE = int(UI_TOP / 5 / 5)
CAPTION = 'YADC'
WHITE = Color(255,255,255)
RED = Color(150,0,0)
GREEN = Color(0,150,0)
