"""
powershell -executionpolicy bypass;
..\..\virtualenv\sgtktest\Scripts\activate.ps1;
cd tests;
$env:SHOTGUN_REPOS_ROOT='..\..';
pytest
"""

if False:
    import sys
    sys.path.append("D:\\python_libs")
    import ptvsd
    ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
    ptvsd.wait_for_attach()

#####

from tank_test.tank_test_base import setUpModule  # noqa
from tank_test.tank_test_base import TankTestBase

from tank_vendor import six
import sgtk

class TestNestedDialogs(TankTestBase):

    cmd_names = ['Test Nested Modal Dialogs']

    def setUp(self):
        super(TestNestedDialogs, self).setUp()
        self.setup_fixtures()

        context = sgtk.Context(self.tk, project=self.project)

        self.engine = sgtk.platform.start_engine("tk-shotgun", self.tk, context)
        self.addCleanup(self.engine.destroy)

        assert self.engine.has_qt4, "engine doesn't have qt"

        self._app = sgtk.platform.qt.QtGui.QApplication.instance() or sgtk.platform.qt.QtGui.QApplication(
            []
        )

    def test_register_cmds(self):
        for name in self.cmd_names:
            assert name in self.engine.commands.keys()

    def test_run_cmds(self):
        for name in self.cmd_names:
            cmd = self.engine.commands[name]
            cmd['callback']()
