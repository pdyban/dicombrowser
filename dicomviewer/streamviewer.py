from .iviewer import IViewer
import sys


class StreamViewer(IViewer):
    def __init__(self, directory, select_tags, stream=sys.stdout):
        super(StreamViewer, self).__init__(directory=directory, select_tags=select_tags)
        self.stream = stream
        self.separator = '\t'

    def parse(self):
        lines = []
        # header line
        line = ['Filename'] + [tag for tag in self.select_tags]
        lines.append(line)

        # for each file
        for fname in self.browser:
            line = [fname] + [self.browser[fname][tag] for tag in self.select_tags]
            lines.append(line)

        return lines

    def draw(self):
        lines = self.parse()

        col_width = []
        for column in range(len(lines[0])):
            col_width.append(max(len(line[column]) for line in lines) + 2)

        # output to stream
        for line in lines:
            self.stream.write(self.separator.join(word.ljust(col_width[column]) for column, word in enumerate(line)))
            self.stream.write('\n')
