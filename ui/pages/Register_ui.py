# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Register.ui'
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

class Ui_RegisterWindow(object):
    def setupUi(self, RegisterWindow):
        if not RegisterWindow.objectName():
            RegisterWindow.setObjectName(u"RegisterWindow")
        RegisterWindow.resize(850, 700)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(RegisterWindow.sizePolicy().hasHeightForWidth())
        RegisterWindow.setSizePolicy(sizePolicy)
        RegisterWindow.setMinimumSize(QSize(850, 700))
        RegisterWindow.setMaximumSize(QSize(850, 700))
        RegisterWindow.setStyleSheet(u"#RegisterWindow {\n"
"	border-image: url(:/ui/res/bg.png);\n"
"}\n"
"\n"
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
        self.gridLayout_2 = QGridLayout(RegisterWindow)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_4 = QSpacerItem(20, 39, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(238, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.centralWidget = QWidget(RegisterWindow)
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
        self.verticalSpacer = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 30, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.lavelll = QLabel(self.centralWidget)
        self.lavelll.setObjectName(u"lavelll")
        font1 = QFont()
        font1.setPointSize(18)
        font1.setBold(True)
        self.lavelll.setFont(font1)
        self.lavelll.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.lavelll, 1, 1, 1, 1)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setSpacing(20)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_singup = QLabel(self.centralWidget)
        self.label_singup.setObjectName(u"label_singup")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_singup.sizePolicy().hasHeightForWidth())
        self.label_singup.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setPointSize(10)
        self.label_singup.setFont(font2)
        self.label_singup.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.label_singup, 6, 0, 1, 1)

        self.btn_singup = QPushButton(self.centralWidget)
        self.btn_singup.setObjectName(u"btn_singup")
        self.btn_singup.setStyleSheet(u"QPushButton{\n"
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

        self.gridLayout_3.addWidget(self.btn_singup, 5, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_username_2 = QLabel(self.centralWidget)
        self.label_username_2.setObjectName(u"label_username_2")
        sizePolicy2.setHeightForWidth(self.label_username_2.sizePolicy().hasHeightForWidth())
        self.label_username_2.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(False)
        self.label_username_2.setFont(font3)

        self.verticalLayout_2.addWidget(self.label_username_2)

        self.lineEdit_username = QLineEdit(self.centralWidget)
        self.lineEdit_username.setObjectName(u"lineEdit_username")
        self.lineEdit_username.setMinimumSize(QSize(250, 0))

        self.verticalLayout_2.addWidget(self.lineEdit_username)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_password_5 = QLabel(self.centralWidget)
        self.label_password_5.setObjectName(u"label_password_5")
        sizePolicy2.setHeightForWidth(self.label_password_5.sizePolicy().hasHeightForWidth())
        self.label_password_5.setSizePolicy(sizePolicy2)
        self.label_password_5.setFont(font3)

        self.verticalLayout_5.addWidget(self.label_password_5)

        self.lineEdit_confirmPassword = QLineEdit(self.centralWidget)
        self.lineEdit_confirmPassword.setObjectName(u"lineEdit_confirmPassword")
        self.lineEdit_confirmPassword.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_5.addWidget(self.lineEdit_confirmPassword)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 3, 0, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(5)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_password_3 = QLabel(self.centralWidget)
        self.label_password_3.setObjectName(u"label_password_3")
        sizePolicy2.setHeightForWidth(self.label_password_3.sizePolicy().hasHeightForWidth())
        self.label_password_3.setSizePolicy(sizePolicy2)
        self.label_password_3.setFont(font3)

        self.verticalLayout_3.addWidget(self.label_password_3)

        self.lineEdit_email = QLineEdit(self.centralWidget)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setEchoMode(QLineEdit.EchoMode.Normal)

        self.verticalLayout_3.addWidget(self.lineEdit_email)


        self.gridLayout_3.addLayout(self.verticalLayout_3, 1, 0, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setSpacing(5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_password_4 = QLabel(self.centralWidget)
        self.label_password_4.setObjectName(u"label_password_4")
        sizePolicy2.setHeightForWidth(self.label_password_4.sizePolicy().hasHeightForWidth())
        self.label_password_4.setSizePolicy(sizePolicy2)
        self.label_password_4.setFont(font3)

        self.verticalLayout_4.addWidget(self.label_password_4)

        self.lineEdit_password = QLineEdit(self.centralWidget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_4.addWidget(self.lineEdit_password)


        self.gridLayout_3.addLayout(self.verticalLayout_4, 2, 0, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(5)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_password_6 = QLabel(self.centralWidget)
        self.label_password_6.setObjectName(u"label_password_6")
        sizePolicy2.setHeightForWidth(self.label_password_6.sizePolicy().hasHeightForWidth())
        self.label_password_6.setSizePolicy(sizePolicy2)
        self.label_password_6.setFont(font3)

        self.verticalLayout_6.addWidget(self.label_password_6)

        self.lineEdit_phone = QLineEdit(self.centralWidget)
        self.lineEdit_phone.setObjectName(u"lineEdit_phone")
        self.lineEdit_phone.setEchoMode(QLineEdit.EchoMode.Normal)

        self.verticalLayout_6.addWidget(self.lineEdit_phone)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 4, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_3, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)


        self.gridLayout_2.addWidget(self.centralWidget, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(238, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 2, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 38, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)


        self.retranslateUi(RegisterWindow)

        QMetaObject.connectSlotsByName(RegisterWindow)
    # setupUi

    def retranslateUi(self, RegisterWindow):
        RegisterWindow.setWindowTitle(QCoreApplication.translate("RegisterWindow", u"Form", None))
        self.lavelll.setText(QCoreApplication.translate("RegisterWindow", u"Sign Up", None))
        self.label_singup.setText(QCoreApplication.translate("RegisterWindow", u"<html><head/><body><p>Go back to <a href=\"#\"><span style=\" font-weight:700; text-decoration: underline; color:#006357;\">Login</span></a></p></body></html>", None))
        self.btn_singup.setText(QCoreApplication.translate("RegisterWindow", u"Register", None))
        self.label_username_2.setText(QCoreApplication.translate("RegisterWindow", u"Username", None))
        self.lineEdit_username.setPlaceholderText("")
        self.label_password_5.setText(QCoreApplication.translate("RegisterWindow", u"Confirm Password", None))
        self.lineEdit_confirmPassword.setPlaceholderText("")
        self.label_password_3.setText(QCoreApplication.translate("RegisterWindow", u"Email", None))
        self.lineEdit_email.setPlaceholderText("")
        self.label_password_4.setText(QCoreApplication.translate("RegisterWindow", u"Password", None))
        self.lineEdit_password.setPlaceholderText("")
        self.label_password_6.setText(QCoreApplication.translate("RegisterWindow", u"Phone", None))
        self.lineEdit_phone.setPlaceholderText("")
    # retranslateUi

