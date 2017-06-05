from .iview import IView
from .iview import IViewModel
from .model import Model


class StreamView(IView):
    def __init__(self, stream):
        super(StreamView, self).__init__()
        self.stream = stream

        self.separator = '\t'

    def update(self):
        if self.viewmodel is None:
            raise AttributeError("A viewmodel has not been connected."
                                 "First connect a viewmodel, then call view.update()")

        lines = self.viewmodel.items

        # compute column width for optimal presentation
        col_width = []
        for column in range(len(lines[0])):
            col_width.append(max(len(line[column]) for line in lines) + 2)

        # output to stream
        for line in lines:
            self.stream.write(self.separator.join(word.ljust(col_width[column]) for column, word in enumerate(line)))
            self.stream.write('\n')


class StreamViewModel(IViewModel):
    def __init__(self, model, view):
        super(StreamViewModel, self).__init__(model, view)

    def build(self):
        self.items = []

        # header line
        headers = ['Filename'] + [tag for tag in self.model.select_tags]
        self.items.append(headers)

        # for each file
        for fname in self.model.items:
            line = [fname] + [self.model.items[fname][tag] for tag in self.model.select_tags]
            self.items.append(line)
