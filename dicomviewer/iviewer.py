import dicombrowser


class IViewer(object):
    def __init__(self, directory, select_tags):
        super(IViewer, self).__init__()
        self.directory = directory
        self.select_tags = select_tags
        if select_tags is None or len(select_tags) < 1:
            raise AttributeError("Please specify at least one DICOM tag.")

        self.browser = dicombrowser.browse(directory, select_tags=select_tags)

    def parse(self):
        """
        Parses the browser and prepares view's internal model representation that canbe directly used for drawing.

        :return: list of lines.
        """
        raise NotImplementedError()

    def draw(self):
        """
        Main function of the viewer, draws the contents of the model.
        :return:
        """
        raise NotImplementedError()
