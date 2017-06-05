from .streamview import StreamView, StreamViewModel


class FileView(StreamView):
    def __init__(self, filestream):
        super(FileView, self).__init__(stream=filestream)


class FileViewModel(StreamViewModel):
    def __init__(self, model, view):
        super(FileViewModel, self).__init__(model, view)
