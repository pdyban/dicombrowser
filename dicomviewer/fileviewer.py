from .streamviewer import StreamViewer


class FileViewer(StreamViewer):
    def __init__(self, filestream, directory, select_tags):
        super(FileViewer, self).__init__(directory=directory, select_tags=select_tags, stream=filestream)
