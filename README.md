Shotgun toolkit test app to demonstrate how a nested modal dialog will close its parent.

Reproduce:
- add the companion Shotgun Toolkit config to a test project's pipeline configurations:
    sgtk:descriptor:...
- open shotgun desktop
- open browser, goto Assets page
- select an asset and right-mouse click the "Test Nested Modal Dialogs" command
- in the first dialog (akin to Connection) click OK
- an error dialog pops, click OK
- in the first dialog click Browse...
- click Ok on the second (Browse) dialog
- both dialogs will close

The event loops of both the inner and outer modal dialogs are quitting.

Per documentation their event loops should only exit when their window closes.

This may be related to the odd way the Ok and Browse actions are 