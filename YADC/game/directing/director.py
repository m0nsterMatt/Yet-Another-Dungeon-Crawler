class Director:
    """
    Someone who directs the game.
    
    The responsibility of Director is to control the sequence of play.
    
    Attributes:
        _video_service (VideoService): for providing video output
    """

    def __init__(self, video_service):
        """
        Constructs a new Director using the specified video service.
        
        Args:
            video_service (VideoService): an instance of VideoService
        """
        self._video_service = video_service

    def start_game(self, cast, script):
        """
        Starts the game using the given cast and script. Runs the main
        game loop.
        
        Args:
            cast (Cast): the cast of Actors
            script (Script): the script of Actions
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._execute_actions('input', cast, script)
            self._execute_actions('update', cast, script)
            self._execute_actions('output', cast, script)
        self._video_service.close_window()

    def _execute_actions(self, group, cast, script):
        """
        Calls execute for each action in the given group.
        
        Args:
            group (string): the name of the group
            cast (Cast): the cast of Actors
            script (Script): the script of Actions
        """
        actions = script.get_items(group)
        for action in actions:
            action.execute(cast, script)
