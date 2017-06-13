from .consoleview import ConsoleView, ConsoleViewModel
from .streamview import StreamView, StreamViewModel
from .fileview import FileView, FileViewModel
from .csvview import CSVView, CSVViewModel
try:
  from .webview import WebView, WebViewModel
except ModuleNotFoundError as e:
  from warnings import warn
  warn('WebView is not available. Reason %s' % ( str(e), ))  
from .model import Model


if __name__ == '__main__':
    pass
