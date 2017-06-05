import dicombrowser


class IView(object):
    def __init__(self, directory, select_tags):
        super(IView, self).__init__()
        self.directory = directory
        self.select_tags = select_tags
        self.model = None
        if select_tags is None or len(select_tags) < 1:
            raise AttributeError("Please specify at least one DICOM tag.")

    def build_model(self):
        """
        Builds the model component in MVVM pattern.

        Launches DicomBrowser and builds the domain model representation.
        """
        self.model = dicombrowser.browse(self.directory, select_tags=self.select_tags)

    def build_viewmodel(self):
        """
        Builds the viewmodel component in MVVM pattern.
        """
        raise NotImplementedError()

    def draw_model(self):
        """
        Main function of the viewer, draws the contents of the model.
        :return:
        """
        raise NotImplementedError()


class IViewModel(object):
    """
    The ViewModel component in MVVM pattern.
    """
    def __init__(self):
        super(IViewModel, self).__init__()
