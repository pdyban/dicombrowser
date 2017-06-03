import dicombrowser


class IViewer(object):
    def __init__(self, directory, select_tags=None):
        super(IViewer, self).__init__()
        self.directory = directory
        self.select_tags = select_tags
        self.browser = dicombrowser.browse(directory, select_tags=select_tags)

    def draw(self):
        """
        Main function of the viewer, draws the contents of the model.
        :return:
        """
        raise NotImplementedError()
