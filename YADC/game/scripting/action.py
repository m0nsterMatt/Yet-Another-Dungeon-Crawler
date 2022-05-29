class Action:
    """
    A thing that is done.
    The responsibility of Action is to do something essential for the
    game. It has one method, execute(), which should be overridden by
    derived classes.
    """

    def execute(self, cast, script):
        """
        Executes something that is essential for the game. This method
        should be overridden by derived classes.
        """
        pass