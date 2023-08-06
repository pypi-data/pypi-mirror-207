""" Application template to be used to build own nice python applications
Copyright Nanosurf AG 2021
License - MIT
"""

import sys
import os
import PySide6
import nanosurf as nsf

import module, gui

MyCompany = "Nanosurf"
MyAppName = "SPM Monitoring "

class MyApp(nsf.frameworks.qt_app.ApplicationBase):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def do_startup(self):
        self.add_module(module.WorkerModule(self, gui.Screen()))
        self.show_message("Ready")
        
if __name__ == "__main__":
    App = MyApp(MyCompany, MyAppName, os.path.abspath(__file__), [])
    App.start_app()
    sys.exit(App.execute())

