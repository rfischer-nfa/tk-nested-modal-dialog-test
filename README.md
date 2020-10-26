Shotgun toolkit test app to demonstrate how:
a nested modal dialog will close its parent
*if a busy dialog is active*.

Reproduce:
- add the companion Shotgun Toolkit config to a test project's pipeline configurations:
    sgtk:descriptor:...
- open shotgun desktop
- open browser, goto Assets page
- select an asset and right-mouse click the "Test Nested Modal Dialogs" command
- in the first modal dialog click OK
- a second modal dialog pops, click OK
- both dialogs will close

The event loops of both the inner and outer modal dialogs are quitting.

Per documentation their event loops should only exit when their window closes.

Calling engine.clear_busy() before show_modal fixes this.
