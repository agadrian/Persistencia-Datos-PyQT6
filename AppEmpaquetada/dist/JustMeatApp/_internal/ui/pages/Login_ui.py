# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)
import resources_rc

class Ui_LoginWindow(object):
    def setupUi(self, LoginWindow):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.setWindowModality(Qt.WindowModality.NonModal)
        LoginWindow.resize(850, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(LoginWindow.sizePolicy().hasHeightForWidth())
        LoginWindow.setSizePolicy(sizePolicy)
        LoginWindow.setMinimumSize(QSize(850, 700))
        LoginWindow.setMaximumSize(QSize(850, 700))
        LoginWindow.setStyleSheet(u"\n"
"#centralWidget {\n"
"	background-color: #FFFFFF;\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"	border: 1px solid gray;\n"
"	border-radius: 6px;\n"
"	padding-left: 5px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"\n"
"\n"
"QLabel {\n"
"	color: #5A5A5A;\n"
"}")
        self.gridLayout_2 = QGridLayout(LoginWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 147, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(235, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.centralWidget = QWidget(LoginWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralWidget.sizePolicy().hasHeightForWidth())
        self.centralWidget.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(11)
        self.centralWidget.setFont(font)
        self.gridLayout = QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.verticalSpacer = QSpacerItem(20, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(20)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_username = QLabel(self.centralWidget)
        self.label_username.setObjectName(u"label_username")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy2)
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(False)
        self.label_username.setFont(font1)

        self.verticalLayout.addWidget(self.label_username)

        self.lineEdit_username = QLineEdit(self.centralWidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMinimumSize(QSize(250, 0))

        self.verticalLayout.addWidget(self.lineEdit_username)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_password = QLabel(self.centralWidget)
        self.label_password.setObjectName(u"label_password")
        sizePolicy2.setHeightForWidth(self.label_password.sizePolicy().hasHeightForWidth())
        self.label_password.setSizePolicy(sizePolicy2)
        self.label_password.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_password)

        self.lineEdit_password = QLineEdit(self.centralWidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.lineEdit_password)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 1, 0, 1, 1)

        self.btn_login = QPushButton(self.centralWidget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setStyleSheet(u"QPushButton{\n"
"	background-color: #34D481;\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 13px;\n"
"	height: 30px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #28a766; \n"
"}")

        self.gridLayout_3.addWidget(self.btn_login, 2, 0, 1, 1)

        self.label_singup = QLabel(self.centralWidget)
        self.label_singup.setObjectName(u"label_singup")
        sizePolicy2.setHeightForWidth(self.label_singup.sizePolicy().hasHeightForWidth())
        self.label_singup.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(10)
        self.label_singup.setFont(font2)
        self.label_singup.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_singup, 3, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(27, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 19, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.lavelll = QLabel(self.centralWidget)
        self.lavelll.setObjectName(u"lavelll")
        font3 = QFont()
        font3.setPointSize(18)
        font3.setBold(True)
        self.lavelll.setFont(font3)
        self.lavelll.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lavelll, 1, 1, 1, 1)


        self.gridLayout_2.addWidget(self.centralWidget, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(235, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 146, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.retranslateUi(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
    # setupUi

    def retranslateUi(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"Form", None))
        self.label_username.setText(QCoreApplication.translate("LoginWindow", u"Email", None))
        self.lineEdit_username.setPlaceholderText("")
        self.label_password.setText(QCoreApplication.translate("LoginWindow", u"Password", None))
        self.lineEdit_password.setPlaceholderText("")
        self.btn_login.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
        self.label_singup.setText(QCoreApplication.translate("LoginWindow", u"<html><head/><body><p>Not a memeber? <a href=\"#\"><span style=\" font-weight:700; text-decoration: underline; color:#006357;\">Sign Up</span></a></p></body></html>", None))
        self.lavelll.setText(QCoreApplication.translate("LoginWindow", u"Sign In", None))
    # retranslateUi

