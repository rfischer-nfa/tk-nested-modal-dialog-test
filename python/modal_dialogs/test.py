import sgtk
from sgtk.platform.qt import QtCore, QtGui

class ConnectionForm(QtGui.QWidget):

    ok_clicked = QtCore.Signal(QtGui.QWidget)

    def __init__(self, postinitfn, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.exit_code = QtGui.QDialog.Rejected
        self.first_time = True
        #
        self.setObjectName("ConnectionForm")
        self.resize(461, 279)

        self.horizLayout = QtGui.QHBoxLayout(self)
        self.horizLayout.setSpacing(4)
        self.horizLayout.setContentsMargins(0, 0, 0, 0)
        self.horizLayout.setObjectName("horizLayout")

        self.ok_btn = QtGui.QPushButton("Ok", self)
        self.ok_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.horizLayout.addWidget(self.ok_btn)

        self.ok_btn.clicked.connect(self.on_ok)

        postinitfn(self)

    def on_ok(self):
        self.exit_code = QtGui.QDialog.Accepted
        self.ok_clicked.emit(self)
        self.exit_code = QtGui.QDialog.Rejected

class ValidityDialog(QtGui.QWidget):
    ok_clicked = QtCore.Signal(QtGui.QWidget)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        #
        self.setObjectName("ValidityDialog")
        self.resize(361, 179)

        self.horizLayout = QtGui.QHBoxLayout(self)
        self.horizLayout.setSpacing(4)
        self.horizLayout.setContentsMargins(0, 0, 0, 0)
        self.horizLayout.setObjectName("horizLayout")

        self.ok_btn = QtGui.QPushButton("Ok", self)
        self.ok_btn.setMinimumSize(QtCore.QSize(100, 0))
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.horizLayout.addWidget(self.ok_btn)

        self.ok_btn.clicked.connect(self.on_ok)

    def on_ok(self):
        self._exit_code = QtGui.QDialog.Accepted
        self.close()

#

import threading
_g_connection_lock = threading.RLock()

def connect():
    global _g_connection_lock
    _g_connection_lock.acquire()
    try:
        raise ValueError(2)
    except ValueError:
        if True:
            return connect_with_dlg()
        else:
            raise
    finally:
        _g_connection_lock.release()

def connect_with_dlg():
    global _g_connection_lock
    _g_connection_lock.acquire()
    try:
        app = sgtk.platform.current_bundle()
        return app.engine.execute_in_main_thread(_connect_with_dlg)
    finally:
        _g_connection_lock.release()

def _connect_with_dlg():
    app = sgtk.platform.current_bundle()
    result, widget = app.engine.show_modal("Connection Form", app, ConnectionForm, setup_open_dlg)
    print result, widget

def setup_open_dlg(widget):
    widget.ok_clicked.connect(on_open_clicked)

def on_open_clicked(widget):
    if widget.first_time:
        #QtGui.QMessageBox.information(widget, "Invalid!", "Workspace not valid")
        app = sgtk.platform.current_bundle()
        app.engine.show_modal('Invalid!', app, ValidityDialog)
        widget.first_time = False
    else:
        widget.close()
