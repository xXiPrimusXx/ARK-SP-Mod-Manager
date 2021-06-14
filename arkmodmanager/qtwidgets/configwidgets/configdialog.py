from arkmodmanager.generated_ui.ui_configdialog import Ui_configDialog
from PySide6.QtWidgets import QDialog, QFileDialog
from PySide6.QtCore import Slot, Signal


class ConfigDialog(QDialog):

    accepted = Signal(str, str, bool)
    rejected = Signal()

    def __init__(self, parent=None):
        super(ConfigDialog, self).__init__(parent)
        self.ui = Ui_configDialog()
        self.ui.setupUi(self)

    @Slot()
    def browseInstallation(self):
        self.ui.installLineEdit.setText(QFileDialog.getExistingDirectory(self))

    @Slot()
    def browseSave(self):
        self.ui.profileLineEdit.setText(QFileDialog.getExistingDirectory(self))

    @Slot()
    def accept(self):
        self.accepted.emit(self.ui.installLineEdit.text(), self.ui.profileLineEdit.text(), True)
        super(ConfigDialog, self).accept()
