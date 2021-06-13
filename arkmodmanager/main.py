import sys
from arkmodmanager.qtwidgets.configwidgets.configdialog import ConfigDialog
from PySide6.QtWidgets import QApplication


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    mainWindow = ConfigDialog()
    mainWindow.show()
    # Run the main Qt loop
    sys.exit(app.exec())
