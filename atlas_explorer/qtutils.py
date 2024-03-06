"""
A module containing Pyside utility functions for
-   loading Qt UI files
-   creating Qt applications and managing the interactive loop in ipython
"""
import logging
from functools import wraps

from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QMetaObject
from PySide6 import QtWidgets
import pyqtgraph as pg

_logger = logging.getLogger(__name__)


class UiLoader(QUiLoader):
    def __init__(self, base_instance):
        QUiLoader.__init__(self, base_instance)
        self.base_instance = base_instance

    def createWidget(self, class_name, parent=None, name=''):
        if parent is None and self.base_instance:
            return self.base_instance
        else:
            # create a new widget for child widgets
            if class_name == "PlotWidget":
                widget = pg.PlotWidget(parent=parent)
            else:
                widget = QUiLoader.createWidget(self, class_name, parent, name)
            if self.base_instance:
                setattr(self.base_instance, name, widget)
            return widget


def load_ui(ui_file, base_instance=None):
    loader = UiLoader(base_instance)
    widget = loader.load(ui_file)
    QMetaObject.connectSlotsByName(widget)
    return widget

def get_main_window():
    """ Get the Main window of a QT application"""
    app = QtWidgets.QApplication.instance()
    return [w for w in app.topLevelWidgets() if isinstance(w, QtWidgets.QMainWindow)][0]


def create_app():
    """Create a Qt application."""
    global QT_APP
    QT_APP = QtWidgets.QApplication.instance()
    if QT_APP is None:  # pragma: no cover
        QT_APP = QtWidgets.QApplication([])
    return QT_APP


def require_qt(func):
    """Function decorator to specify that a function requires a Qt application.
    Use this decorator to specify that a function needs a running
    Qt application before it can run. An error is raised if that is not
    the case.
    """
    @wraps(func)
    def wrapped(*args, **kwargs):
        if not QtWidgets.QApplication.instance():  # pragma: no cover
            _logger.warning("Creating a Qt application.")
            create_app()
        return func(*args, **kwargs)
    return wrapped


@require_qt
def run_app():  # pragma: no cover
    """Run the Qt application."""
    global QT_APP
    return QT_APP.exit(QT_APP.exec_())
