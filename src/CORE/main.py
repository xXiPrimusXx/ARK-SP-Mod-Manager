import sys
from freshInstallWindow import FreshInstallWindow
from PySide6.QtWidgets import QApplication, QDialog, QLineEdit, QPushButton


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    mainWindow = FreshInstallWindow()
    mainWindow.show()
    # Run the main Qt loop
    sys.exit(app.exec())
