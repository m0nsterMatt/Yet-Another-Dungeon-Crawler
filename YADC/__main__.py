from game.casting.rooms import Rooms
from game.casting.hud import HUD
from game.casting.player import Player
from game.casting.screens import Screen

from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.handle_updates_action import HandleUpdatesAction
from game.scripting.draw_actors_action import DrawActorsAction

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.collection import Collection

from constants import *


def main():
    # set up the services
    keyboard_service = KeyboardService()
    video_service = VideoService()

    # create the cast
    cast = Collection()
    cast.add_item('ui', HUD())
    cast.add_item('ui', Screen())
    cast.add_item('player', Player())
    cast.add_item('enemies', Rooms())

    # create the script
    script = Collection()
    script.add_item('input', ControlActorsAction(keyboard_service))
    script.add_item('update', HandleUpdatesAction())
    script.add_item('output', DrawActorsAction(video_service))

    # start the game
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == '__main__':
    main()
