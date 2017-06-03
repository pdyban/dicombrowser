from .fileviewer import FileViewer
import csv
from collections import OrderedDict


class CSVViewer(FileViewer):
    def __init__(self, filestream, directory, select_tags, delimiter=';', lineterminator='\n'):
        super(CSVViewer, self).__init__(directory=directory, select_tags=select_tags, filestream=filestream)
        self.delimiter = delimiter
        self.lineterminator = lineterminator

    def parse(self):
        lines = []

        # for each file
        for fname in self.browser:
            line = {tag: self.browser[fname][tag] for tag in self.select_tags}
            line['Filename'] = fname
            lines.append(line)

        return lines

    def draw(self):
        headers = ['Filename'] + self.select_tags
        writer = csv.DictWriter(self.stream, headers,
                                delimiter=self.delimiter,
                                lineterminator=self.lineterminator)

        writer.writeheader()
        for line in self.parse():
            writer.writerow(line)
