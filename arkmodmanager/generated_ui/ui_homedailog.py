# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'homeDailog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_homeDialog(object):
    def setupUi(self, homeDialog):
        if not homeDialog.objectName():
            homeDialog.setObjectName(u"homeDialog")
        homeDialog.resize(400, 292)
        self.verticalLayout_2 = QVBoxLayout(homeDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setObjectName(u"mainLayout")
        self.label = QLabel(homeDialog)
        self.label.setObjectName(u"label")

        self.mainLayout.addWidget(self.label)

        self.installLineEdit = QLineEdit(homeDialog)
        self.installLineEdit.setObjectName(u"installLineEdit")
        self.installLineEdit.setReadOnly(True)

        self.mainLayout.addWidget(self.installLineEdit)

        self.label_2 = QLabel(homeDialog)
        self.label_2.setObjectName(u"label_2")

        self.mainLayout.addWidget(self.label_2)

        self.profileLineEdit = QLineEdit(homeDialog)
        self.profileLineEdit.setObjectName(u"profileLineEdit")
        self.profileLineEdit.setReadOnly(True)

        self.mainLayout.addWidget(self.profileLineEdit)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.mainLayout.addItem(self.verticalSpacer)

        self.buttonLayout = QHBoxLayout()
        self.buttonLayout.setObjectName(u"buttonLayout")
        self.configBtn = QPushButton(homeDialog)
        self.configBtn.setObjectName(u"configBtn")

        self.buttonLayout.addWidget(self.configBtn)

        self.closeBtn = QPushButton(homeDialog)
        self.closeBtn.setObjectName(u"closeBtn")

        self.buttonLayout.addWidget(self.closeBtn)


        self.mainLayout.addLayout(self.buttonLayout)


        self.verticalLayout_2.addLayout(self.mainLayout)


        self.retranslateUi(homeDialog)

        QMetaObject.connectSlotsByName(homeDialog)
    # setupUi

    def retranslateUi(self, homeDialog):
        homeDialog.setWindowTitle(QCoreApplication.translate("homeDialog", u"Ark Single Player Mod Manager", None))
        self.label.setText(QCoreApplication.translate("homeDialog", u"Ark Install Path:", None))
        self.label_2.setText(QCoreApplication.translate("homeDialog", u"Mod Profile Path:", None))
        self.configBtn.setText(QCoreApplication.translate("homeDialog", u"Configure", None))
        self.closeBtn.setText(QCoreApplication.translate("homeDialog", u"Close", None))
    # retranslateUi

