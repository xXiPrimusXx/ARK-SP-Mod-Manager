from PySide6.QtCore import Slot
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog


class FreshInstallWindow(QDialog):

    def __init__(self, parent=None):
        super(FreshInstallWindow, self).__init__(parent)
        self.setWindowTitle("Ark SP Mod Manager")
        self.lineEdit = QLineEdit("Enter the path to your Ark installation here.")
        self.configBtn = QPushButton("Continue")
        self.configBtn.released.connect(self.config_btn_released)
        layout = QVBoxLayout(self)
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.configBtn)
        self.setLayout(layout)
        self.setMinimumSize(800, 600)

    def config_btn_released(self):
        self.lineEdit.setText(QFileDialog.getExistingDirectory(self))
