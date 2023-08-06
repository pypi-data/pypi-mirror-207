""" The application base class of the application framework
Copyright Nanosurf AG 2021
License - MIT
"""

import sys
import os
import ctypes
import logging
import pathlib

from nanosurf.lib.gui.import_helper import import_pyside2_if_none_is_detected
if import_pyside2_if_none_is_detected():
    from PySide2.QtWidgets import QApplication
    from PySide2.QtCore import QSettings
else:
    from PySide6.QtWidgets import QApplication
    from PySide6.QtCore import QSettings


import nanosurf as nsf
from nanosurf.lib.frameworks.qt_app.app_gui import AppWindow
from nanosurf.lib.frameworks.qt_app.app_common import MsgType
from nanosurf.lib.frameworks.qt_app.module_base import ModuleBase, ModuleScreen
from nanosurf.lib.datatypes.prop_val import PropStore, PropVal

dir_name_log = "log"
dir_name_config = "config"

class AppSettings(PropStore):
    Logging  = PropVal(True)
    LoadLastSettings = PropVal(True)
    ActiveModuleIndex = PropVal(int(0))

class ApplicationBase(QApplication):
    def __init__(self, company: str, app_name_short: str, main_path:pathlib.Path, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.company = company
        self.app_name_long = app_name_short
        self.app_name = app_name_short.replace(" ","_")
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_name_short)
        self.is_in_debugging_mode = (getattr(sys, 'gettrace', lambda : None)() is not None)

        """ Standard registry connection is defined here for further usage also by modules"""
        self.registry = QSettings(self.company, self.app_name)

        """ Standard files and folders are defined here for further usage also by modules"""
        self.main_path = pathlib.Path(main_path).parent
        self.framework_path = pathlib.Path(os.path.abspath(__file__)).parent
        self.app_data_path = pathlib.Path(os.path.expandvars(r'%LOCALAPPDATA%')) / pathlib.Path(self.company) / pathlib.Path(self.app_name) 
        self.log_path = self.app_data_path / dir_name_log
        self.config_path = self.app_data_path / dir_name_config
        self.config_file =  self.config_path / "last_config.ini"

        """ application specific settings """
        self.config_section = "Application"
        self.resource_path = self.framework_path 
        self.settings = AppSettings()
        self.modules:dict[ModuleBase] = {}

    def start_app(self):
        nsf.util.fileutil.create_folder(self.config_path)
        nsf.datatypes.prop_val.load_from_ini_file(self.settings, self.config_file, self.config_section)   
        self.setup_logger()
        self.appwindow = AppWindow(self)
        self.appwindow.create_gui(self.resource_path / "app_stylesheet.qss", self.resource_path / "app_icon.ico")
        self.lastWindowClosed.connect(self.quit_app)
        self.do_startup()
        self.appwindow.activate_screen(self.settings.ActiveModuleIndex.value)
        self.appwindow.show()
        self.logger.info("App running...")

    def quit_app(self):
        self.stop_modules()
        self.do_shutdown()
        nsf.datatypes.prop_val.save_to_ini_file(self.settings, self.config_file, self.config_section)   

    def do_startup(self):
        raise NotImplementedError(f"Subclass of '{self.__class__.__name__}' has to implement '{sys._getframe().f_code.co_name}()'")
   
    def do_shutdown(self):
        pass

    def execute(self):
        if import_pyside2_if_none_is_detected():
            self.exec_()
        else:
            self.exec()

    def save_settings(self, module: ModuleBase):
        if isinstance(module.settings, PropStore):
            nsf.datatypes.prop_val.save_to_ini_file(module.settings,self.config_file, module.name)
 
    def load_settings(self, module: ModuleBase):
        if isinstance(module.settings, PropStore):
            if self.settings.LoadLastSettings.value:
                nsf.datatypes.prop_val.load_from_ini_file(module.settings, self.config_file, module.name)
 
    def setup_logger(self, logfile: pathlib.Path = pathlib.Path("latest.log")):   
        """
        Setup Logger if needed and differ between consol and file output
        set up logging to file and choose logger level (from highest level to lowest: Debug, info, warning, error, critical)
        """ 
        if self.settings.Logging.value:
            nsf.util.fileutil.create_folder(self.log_path)
            logfilepath = str(self.log_path / logfile) 
            logging.basicConfig(level=logging.DEBUG,
                                format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                                datefmt='%m-%d %H:%M:%S',
                                filename=logfilepath,
                                filemode='w')
            console = logging.StreamHandler()
            console.setLevel(logging.INFO)
            formatter = logging.Formatter('%(name)-12s %(levelname)-8s %(message)s')
            console.setFormatter(formatter)
            logging.getLogger('').addHandler(console)
        self.logger = logging.getLogger('Application')
        self.logger.setLevel(logging.DEBUG)

    def show_error_message(self, msg:str):
        self.show_message(msg, MsgType.Error)
        
    def show_warn_message(self, msg:str):
        self.show_message(msg,MsgType.Warn)
        
    def show_info_message(self, msg:str):
        self.show_message(msg,MsgType.Info)
        
    def clear_message(self):
        self.appwindow.hide_message()

    def show_message(self, msg: str, msg_type: MsgType = MsgType.Info):
        self.appwindow.show_message(msg, msg_type)

    def add_module(self, new_module: ModuleBase, name:str ="Module", new_screen:ModuleScreen = None):
        new_module.name = name
        if new_screen is not None:
            new_module.ui = new_screen
        self.logger.info(f"Start module: {new_module.name}")
        self.modules[new_module.name] = new_module
        new_module.start()
        if new_module.ui is not None:
            self.add_screen(new_module, new_module.ui, name)
      
    def add_screen(self, module: ModuleBase, new_screen:ModuleScreen, screen_name:str ="Screen"):
        new_screen.create_screen(module)
        self.appwindow.add_screen(new_screen, screen_name)

    def get_module_count(self) -> int:
        return len(self.modules)     

    def activate_module(self, module_index: int):
        self.settings.ActiveModuleIndex.value = module_index
        self.appwindow.set_active_module_by_index(module_index)   
        
    def stop_modules(self):
        for mod in self.modules.values():
            self.logger.info(f"Stop module: {mod.name}")
            mod.stop()

    def activate_debugger_support_for_this_thread(self):
        """ This function has to be called from each new thread to activate debugger support for it"""
        if self.is_in_debugging_mode:
            import debugpy
            debugpy.debug_this_thread()            
 
