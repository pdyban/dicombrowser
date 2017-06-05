import dicombrowser


class IView(object):
    def __init__(self):
        super(IView, self).__init__()
        self.viewmodel = None

    def update(self):
        """
        Main function of the view component in MVVM pattern, draws the contents of the model to the output device.
        :return:
        """
        raise NotImplementedError()


class IViewModel(object):
    """
    The ViewModel component in MVVM pattern.
    """
    def __init__(self, model, view):
        super(IViewModel, self).__init__()

        # connect to model
        self.model = model
        self.model.viewmodels.append(self)

        # connect to view and update
        self.view = view
        self.view.viewmodel = self
        # self.view.update()
