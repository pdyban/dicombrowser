from .iviewer import IViewer
import sys


class StreamViewer(IViewer):
    def __init__(self, directory, select_tags=None, stream=sys.stdout):
        super(StreamViewer, self).__init__(directory=directory, select_tags=select_tags)
        self.stream = stream
        self.separator = '\t'

    def draw(self):
        lines = []
        # header line
        line = ['Filename'] + [tag for tag in self.select_tags]
        lines.append(line)

        # for each file
        for fname in self.browser:
            line = [fname] + [self.browser[fname][tag] for tag in self.select_tags]
            lines.append(line)

        # output to stream
        for line in lines:
            self.stream.write(self.separator.join(line))
            self.stream.write('\n')
