from .streamview import StreamView, StreamViewModel
import sys


class ConsoleView(StreamView):
    """
    Prints contents of the model into the command line.
    """
    def __init__(self):
        super(ConsoleView, self).__init__(stream=sys.stdout)


class ConsoleViewModel(StreamViewModel):
    """
    Connects the model and view together.

    Updates the view if connection successful.
    """
    def __init__(self, model, view):
        super(ConsoleViewModel, self).__init__(model, view)
