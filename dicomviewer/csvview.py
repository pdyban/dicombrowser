from .fileview import FileView, FileViewModel
import csv
from .model import Model


class CSVView(FileView):
    def __init__(self, filestream, delimiter=';', lineterminator='\n'):
        super(CSVView, self).__init__(filestream=filestream)
        self.delimiter = delimiter
        self.lineterminator = lineterminator

    def update(self):
        """
        Draws contents of model into a CSV file.
        """
        headers = self.viewmodel.headers
        items = self.viewmodel.items
        writer = csv.DictWriter(self.stream, headers,
                                delimiter=self.delimiter,
                                lineterminator=self.lineterminator)

        writer.writeheader()
        for line in items:
            writer.writerow(line)


class CSVViewModel(FileViewModel):
    def __init__(self, model, view):
        super(CSVViewModel, self).__init__(model, view)

        self.headers = ['Filename'] + model.select_tags

    def build(self):
        self.items = []

        # for each file
        for fname in self.model.items:
            line = {tag: self.model.items[fname][tag] for tag in self.model.select_tags}
            line['Filename'] = fname
            self.items.append(line)
