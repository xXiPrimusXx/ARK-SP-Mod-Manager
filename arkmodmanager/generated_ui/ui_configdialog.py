# -*- coding: utf-8 -*-

################################################################################
## Form generated_ui from reading UI file 'configDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_configDialog(object):
    def setupUi(self, configDialog):
        if not configDialog.objectName():
            configDialog.setObjectName(u"configDialog")
        configDialog.resize(623, 352)
        self.verticalLayout_2 = QVBoxLayout(configDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.configTextEdit = QTextEdit(configDialog)
        self.configTextEdit.setObjectName(u"configTextEdit")
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.configTextEdit.sizePolicy().hasHeightForWidth())
        self.configTextEdit.setSizePolicy(sizePolicy)
        self.configTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.configTextEdit)

        self.installLabel = QLabel(configDialog)
        self.installLabel.setObjectName(u"installLabel")

        self.verticalLayout.addWidget(self.installLabel)

        self.installLayout = QHBoxLayout()
        self.installLayout.setObjectName(u"installLayout")
        self.installLineEdit = QLineEdit(configDialog)
        self.installLineEdit.setObjectName(u"installLineEdit")

        self.installLayout.addWidget(self.installLineEdit)

        self.installBrowseBtn = QPushButton(configDialog)
        self.installBrowseBtn.setObjectName(u"installBrowseBtn")

        self.installLayout.addWidget(self.installBrowseBtn)


        self.verticalLayout.addLayout(self.installLayout)

        self.profileLabel = QLabel(configDialog)
        self.profileLabel.setObjectName(u"profileLabel")

        self.verticalLayout.addWidget(self.profileLabel)

        self.profileLayout = QHBoxLayout()
        self.profileLayout.setObjectName(u"profileLayout")
        self.profileLineEdit = QLineEdit(configDialog)
        self.profileLineEdit.setObjectName(u"profileLineEdit")

        self.profileLayout.addWidget(self.profileLineEdit)

        self.profileBrowseBtn = QPushButton(configDialog)
        self.profileBrowseBtn.setObjectName(u"profileBrowseBtn")

        self.profileLayout.addWidget(self.profileBrowseBtn)


        self.verticalLayout.addLayout(self.profileLayout)

        self.controlLayout = QHBoxLayout()
        self.controlLayout.setObjectName(u"controlLayout")
        self.acceptBtn = QPushButton(configDialog)
        self.acceptBtn.setObjectName(u"acceptBtn")

        self.controlLayout.addWidget(self.acceptBtn)

        self.cancelBtn = QPushButton(configDialog)
        self.cancelBtn.setObjectName(u"cancelBtn")

        self.controlLayout.addWidget(self.cancelBtn)


        self.verticalLayout.addLayout(self.controlLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(configDialog)
        self.installBrowseBtn.released.connect(configDialog.browseInstallation)
        self.profileBrowseBtn.released.connect(configDialog.browseSave)
        self.acceptBtn.released.connect(configDialog.accept)
        self.cancelBtn.released.connect(configDialog.reject)

        QMetaObject.connectSlotsByName(configDialog)
    # setupUi

    def retranslateUi(self, configDialog):
        configDialog.setWindowTitle(QCoreApplication.translate("configDialog", u"Dialog", None))
        self.configTextEdit.setDocumentTitle("")
        self.configTextEdit.setHtml(QCoreApplication.translate("configDialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">To configure this application please select your installation path for ARK (where you installed ARK with steam) and where you would like to save your mod profiles using the file browser (by clicking browse) or by entering the path in the text box.</span></p></body></html>", None))
        self.installLabel.setText(QCoreApplication.translate("configDialog", u"ARK Installation Path:", None))
        self.installLineEdit.setPlaceholderText(QCoreApplication.translate("configDialog", u"e.g. 'C:\\Program Files (x86)\\Steam\\steamapps\\common\\ARK'", None))
        self.installBrowseBtn.setText(QCoreApplication.translate("configDialog", u"Browse", None))
        self.profileLabel.setText(QCoreApplication.translate("configDialog", u"Profile Save Directory:", None))
        self.profileLineEdit.setPlaceholderText(QCoreApplication.translate("configDialog", u"e.g. 'C:\\Program Files (x86)\\Ark Mod Profiles'", None))
        self.profileBrowseBtn.setText(QCoreApplication.translate("configDialog", u"Browse", None))
        self.acceptBtn.setText(QCoreApplication.translate("configDialog", u"Accept", None))
        self.cancelBtn.setText(QCoreApplication.translate("configDialog", u"Cancel", None))
    # retranslateUi

