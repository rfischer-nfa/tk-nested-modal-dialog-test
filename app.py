import sgtk
from sgtk.platform.qt import QtGui

class TkNestedModalDialogTest(sgtk.platform.Application):
    def init_app(self):
        self.engine.register_command("Test Nested Modal Dialogs", self.sync_workfolder)

    def sync_workfolder(self):
        try:
            self.engine.show_busy('Busy', '...please hold')
            test = self.import_module("modal_dialogs")
            test.connect()
        finally:
            self.engine.clear_busy()
