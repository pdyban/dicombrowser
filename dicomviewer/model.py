from dicombrowser import browse


class Model(list):
    """
    Encapsulates the model that is used in MVVM pattern.
    """
    def __init__(self, directory, select_tags):
        super(Model, self).__init__()
        self.directory = directory
        self.select_tags = select_tags
        self.viewmodels = []

        if select_tags is None or len(select_tags) < 1:
            raise AttributeError("Please specify at least one DICOM tag.")

        self.items = None
        try:
            self.items = browse(directory, select_tags=select_tags)

        except AttributeError:
            pass  # ignore if directory is emtpy or non-existent
