import sys
import os.path
from arkmodmanager.qtwidgets.configwidgets.configdialog import ConfigDialog
from arkmodmanager.qtwidgets.homewidgets.homedialog import HomeDialog
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Slot, Signal


class MainLogic(QMainWindow):

    def __init__(self):
        super(MainLogic, self).__init__()
        self.configure_dialog = ConfigDialog()
        self.home_dialog = HomeDialog()
        self.ark_install_path = ""
        self.profile_install_path = ""

    def show_config_dialog(self):
        self.configure_dialog.accepted.connect(self.show_home_dailog)
        self.configure_dialog.show()

    @Slot(str, str, bool)
    def show_home_dailog(self, set_install_path, set_profile_path, overwrite):
        self.ark_install_path = set_install_path
        self.profile_install_path = set_profile_path
        if overwrite:
            new_config_file = open("ark-sp-mm.cfg", "w")
            new_config_file.write("install_path: " + set_install_path + "\n")
            new_config_file.write("profile_path: " + set_profile_path + "\n")
            new_config_file.close()
        self.home_dialog.set_config_paths(set_install_path, set_profile_path)
        self.home_dialog.ui.configBtn.released.connect(self.show_config_dialog)
        self.home_dialog.ui.closeBtn.released.connect(self.home_dialog.close)
        self.home_dialog.show()


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    main_logic = MainLogic()
    if not os.path.exists(os.getcwd() + "/ark-sp-mm.cfg"):
        main_logic.show_config_dialog()
    else:
        config_file = open("ark-sp-mm.cfg")
        install_path = config_file.readline().removeprefix("install_path: ")
        profile_path = config_file.readline().removeprefix("profile_path: ")
        main_logic.show_home_dailog(install_path, profile_path, False)
    # Run the main Qt loop
    app.exec()
