from arkmodmanager.generated_ui.ui_homedailog import Ui_homeDialog
from PySide6.QtWidgets import QDialog


class HomeDialog(QDialog):

    def __init__(self, parent=None):
        super(HomeDialog, self).__init__(parent)
        self.ui = Ui_homeDialog()
        self.ui.setupUi(self)

    def set_config_paths(self, install_path, profiles_path):
        self.ui.installLineEdit.setText(install_path)
        self.ui.profileLineEdit.setText(profiles_path)
