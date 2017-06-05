from .streamviewer import StreamView
import sys


class ConsoleViewer(StreamView):
    def __init__(self, directory, select_tags):
        super(ConsoleViewer, self).__init__(directory=directory, select_tags=select_tags, stream=sys.stdout)
