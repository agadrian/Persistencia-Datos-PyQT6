# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Home.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1304, 767)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.icons = QWidget(self.centralwidget)
        self.icons.setObjectName(u"icons")
        self.icons.setGeometry(QRect(0, 0, 231, 921))
        self.icons.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}")
        self.label = QLabel(self.icons)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(60, 20, 101, 71))
        self.label.setPixmap(QPixmap(u"../res/logo3.png"))
        self.layoutWidget = QWidget(self.icons)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 130, 211, 621))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_reports = QPushButton(self.layoutWidget)
        self.btn_reports.setObjectName(u"btn_reports")
        self.btn_reports.setAutoFillBackground(False)
        self.btn_reports.setStyleSheet(u"QPushButton:checked{\n"
"	border-radius: 5px;\n"
"	border: 1.5px solid white;\n"
"}")
        icon = QIcon()
        icon.addFile(u"../res/Reports.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_reports.setIcon(icon)
        self.btn_reports.setIconSize(QSize(130, 120))
        self.btn_reports.setCheckable(True)
        self.btn_reports.setChecked(True)
        self.btn_reports.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_reports)

        self.btn_querys = QPushButton(self.layoutWidget)
        self.btn_querys.setObjectName(u"btn_querys")
        self.btn_querys.setAutoFillBackground(False)
        self.btn_querys.setStyleSheet(u"QPushButton:checked{\n"
"	border-radius: 5px;\n"
"	border: 1.5px solid white;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../res/querys3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_querys.setIcon(icon1)
        self.btn_querys.setIconSize(QSize(150, 120))
        self.btn_querys.setCheckable(True)
        self.btn_querys.setChecked(False)
        self.btn_querys.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_querys)

        self.btn_users = QPushButton(self.layoutWidget)
        self.btn_users.setObjectName(u"btn_users")
        self.btn_users.setAutoFillBackground(False)
        self.btn_users.setStyleSheet(u"QPushButton:checked{\n"
"	border-radius: 5px;\n"
"	border: 1.5px solid white;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../res/users4.jpg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_users.setIcon(icon2)
        self.btn_users.setIconSize(QSize(150, 120))
        self.btn_users.setCheckable(True)
        self.btn_users.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_users)

        self.btn_restaurants = QPushButton(self.layoutWidget)
        self.btn_restaurants.setObjectName(u"btn_restaurants")
        self.btn_restaurants.setAutoFillBackground(False)
        self.btn_restaurants.setStyleSheet(u"QPushButton:checked{\n"
"	border-radius: 5px;\n"
"	border: 1.5px solid white;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../res/restaurants4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_restaurants.setIcon(icon3)
        self.btn_restaurants.setIconSize(QSize(150, 120))
        self.btn_restaurants.setCheckable(True)
        self.btn_restaurants.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_restaurants)

        self.btn_dishes = QPushButton(self.layoutWidget)
        self.btn_dishes.setObjectName(u"btn_dishes")
        self.btn_dishes.setAutoFillBackground(False)
        self.btn_dishes.setStyleSheet(u"QPushButton:checked{\n"
"	border-radius: 5px;\n"
"	border: 1.5px solid white;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../res/dish3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_dishes.setIcon(icon4)
        self.btn_dishes.setIconSize(QSize(150, 150))
        self.btn_dishes.setCheckable(True)
        self.btn_dishes.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_dishes)

        self.btn_delivery = QPushButton(self.layoutWidget)
        self.btn_delivery.setObjectName(u"btn_delivery")
        self.btn_delivery.setAutoFillBackground(False)
        self.btn_delivery.setStyleSheet(u"QPushButton:checked{\n"
"	border-radius: 5px;\n"
"	border: 1.5px solid white;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u"../res/delivery3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_delivery.setIcon(icon5)
        self.btn_delivery.setIconSize(QSize(150, 120))
        self.btn_delivery.setCheckable(True)
        self.btn_delivery.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_delivery)

        self.btn_orders = QPushButton(self.layoutWidget)
        self.btn_orders.setObjectName(u"btn_orders")
        self.btn_orders.setAutoFillBackground(False)
        self.btn_orders.setStyleSheet(u"QPushButton:checked{\n"
"	border-radius: 5px;\n"
"	border: 1.5px solid white;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u"../res/orders3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_orders.setIcon(icon6)
        self.btn_orders.setIconSize(QSize(150, 120))
        self.btn_orders.setCheckable(True)
        self.btn_orders.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_orders)

        self.btn_orderDetails = QPushButton(self.layoutWidget)
        self.btn_orderDetails.setObjectName(u"btn_orderDetails")
        self.btn_orderDetails.setAutoFillBackground(False)
        self.btn_orderDetails.setStyleSheet(u"QPushButton:checked{\n"
"	border-radius: 5px;\n"
"	border: 1.5px solid white;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u"../res/orderDetails3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_orderDetails.setIcon(icon7)
        self.btn_orderDetails.setIconSize(QSize(150, 120))
        self.btn_orderDetails.setCheckable(True)
        self.btn_orderDetails.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.btn_orderDetails)

        self.main_screen = QWidget(self.centralwidget)
        self.main_screen.setObjectName(u"main_screen")
        self.main_screen.setGeometry(QRect(250, 90, 1061, 671))
        self.main_screen.setStyleSheet(u"<-- background-color: rgb(255, 170, 0); -->")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(260, 30, 1031, 721))
        self.page_consultas = QWidget()
        self.page_consultas.setObjectName(u"page_consultas")
        self.users_tittle_2 = QLabel(self.page_consultas)
        self.users_tittle_2.setObjectName(u"users_tittle_2")
        self.users_tittle_2.setGeometry(QRect(20, 0, 141, 51))
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(30)
        font.setBold(True)
        self.users_tittle_2.setFont(font)
        self.tableWidget = QTableWidget(self.page_consultas)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 260, 1011, 431))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QTableWidget::item, QTableView::item {\n"
"    background-color: #FFFFFF; \n"
"}\n"
"\n"
"QTableWidget::item:alternate, QTableView::item:alternate {\n"
"    background-color: #F2F2F2; \n"
"}")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(120)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.layoutWidget1 = QWidget(self.page_consultas)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 50, 1118, 211))
        self.gridLayoutQuerys = QGridLayout(self.layoutWidget1)
        self.gridLayoutQuerys.setObjectName(u"gridLayoutQuerys")
        self.gridLayoutQuerys.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        self.label_10.setMinimumSize(QSize(450, 0))
        self.label_10.setMaximumSize(QSize(450, 16777215))
        font1 = QFont()
        font1.setPointSize(13)
        font1.setBold(True)
        self.label_10.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_10)

        self.pushButton_q1 = QPushButton(self.layoutWidget1)
        self.pushButton_q1.setObjectName(u"pushButton_q1")
        self.pushButton_q1.setMinimumSize(QSize(60, 0))
        self.pushButton_q1.setMaximumSize(QSize(60, 16777215))
        self.pushButton_q1.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_q1)


        self.verticalLayout_10.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(450, 0))
        self.label_11.setMaximumSize(QSize(450, 16777215))
        self.label_11.setFont(font1)

        self.horizontalLayout_4.addWidget(self.label_11)

        self.pushButton_q2 = QPushButton(self.layoutWidget1)
        self.pushButton_q2.setObjectName(u"pushButton_q2")
        self.pushButton_q2.setMinimumSize(QSize(60, 0))
        self.pushButton_q2.setMaximumSize(QSize(60, 16777215))
        self.pushButton_q2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")

        self.horizontalLayout_4.addWidget(self.pushButton_q2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(450, 16777215))
        self.label_12.setFont(font1)

        self.horizontalLayout_5.addWidget(self.label_12)

        self.pushButton_q3 = QPushButton(self.layoutWidget1)
        self.pushButton_q3.setObjectName(u"pushButton_q3")
        self.pushButton_q3.setMaximumSize(QSize(60, 16777215))
        self.pushButton_q3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")

        self.horizontalLayout_5.addWidget(self.pushButton_q3)


        self.verticalLayout_10.addLayout(self.horizontalLayout_5)


        self.gridLayoutQuerys.addLayout(self.verticalLayout_10, 0, 0, 1, 1)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(25)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.pushButton_q4 = QPushButton(self.layoutWidget1)
        self.pushButton_q4.setObjectName(u"pushButton_q4")
        self.pushButton_q4.setMinimumSize(QSize(20, 0))
        self.pushButton_q4.setMaximumSize(QSize(60, 16777215))
        self.pushButton_q4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")

        self.horizontalLayout_10.addWidget(self.pushButton_q4)

        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)

        self.horizontalLayout_10.addWidget(self.label_13)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(25)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.pushButton_q5 = QPushButton(self.layoutWidget1)
        self.pushButton_q5.setObjectName(u"pushButton_q5")
        self.pushButton_q5.setMinimumSize(QSize(60, 0))
        self.pushButton_q5.setMaximumSize(QSize(60, 16777215))
        self.pushButton_q5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")

        self.horizontalLayout_11.addWidget(self.pushButton_q5)

        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)

        self.horizontalLayout_11.addWidget(self.label_14)


        self.verticalLayout_11.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setSpacing(25)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.pushButton_q6 = QPushButton(self.layoutWidget1)
        self.pushButton_q6.setObjectName(u"pushButton_q6")
        self.pushButton_q6.setMaximumSize(QSize(60, 16777215))
        self.pushButton_q6.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"}")

        self.horizontalLayout_12.addWidget(self.pushButton_q6)

        self.label_15 = QLabel(self.layoutWidget1)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)

        self.horizontalLayout_12.addWidget(self.label_15)


        self.verticalLayout_11.addLayout(self.horizontalLayout_12)


        self.gridLayoutQuerys.addLayout(self.verticalLayout_11, 0, 1, 1, 1)

        self.stackedWidget.addWidget(self.page_consultas)
        self.page_home = QWidget()
        self.page_home.setObjectName(u"page_home")
        self.label_16 = QLabel(self.page_home)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(20, 60, 281, 41))
        font2 = QFont()
        font2.setPointSize(13)
        self.label_16.setFont(font2)
        self.label_17 = QLabel(self.page_home)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(20, 10, 311, 51))
        font3 = QFont()
        font3.setPointSize(30)
        font3.setBold(True)
        self.label_17.setFont(font3)
        self.layoutWidget2 = QWidget(self.page_home)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(30, 180, 951, 311))
        self.horizontalLayout_13 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_9 = QLabel(self.layoutWidget2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(15)
        font4.setBold(True)
        self.label_9.setFont(font4)
        self.label_9.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_9)

        self.pushButton_crossAnalysis = QPushButton(self.layoutWidget2)
        self.pushButton_crossAnalysis.setObjectName(u"pushButton_crossAnalysis")
        self.pushButton_crossAnalysis.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(100, 100, 100);\n"
"}")

        self.verticalLayout_9.addWidget(self.pushButton_crossAnalysis)


        self.verticalLayout_8.addLayout(self.verticalLayout_9)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget2)
        self.label_5.setObjectName(u"label_5")
        sizePolicy2.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy2)
        self.label_5.setFont(font4)
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.label_5)

        self.pushButton_getTopRestaurants = QPushButton(self.layoutWidget2)
        self.pushButton_getTopRestaurants.setObjectName(u"pushButton_getTopRestaurants")
        self.pushButton_getTopRestaurants.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(100, 100, 100);\n"
"}")

        self.verticalLayout_4.addWidget(self.pushButton_getTopRestaurants)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget2)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setFont(font4)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_5.addWidget(self.label_6)

        self.pushButton_getConsum = QPushButton(self.layoutWidget2)
        self.pushButton_getConsum.setObjectName(u"pushButton_getConsum")
        self.pushButton_getConsum.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(100, 100, 100);\n"
"}")

        self.verticalLayout_5.addWidget(self.pushButton_getConsum)


        self.verticalLayout_8.addLayout(self.verticalLayout_5)


        self.horizontalLayout_13.addLayout(self.verticalLayout_8)

        self.horizontalSpacer = QSpacerItem(50, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget2)
        self.label_7.setObjectName(u"label_7")
        sizePolicy2.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy2)
        self.label_7.setFont(font4)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_6.addWidget(self.label_7)

        self.pushButton_getbutn = QPushButton(self.layoutWidget2)
        self.pushButton_getbutn.setObjectName(u"pushButton_getbutn")
        self.pushButton_getbutn.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(100, 100, 100);\n"
"}")

        self.verticalLayout_6.addWidget(self.pushButton_getbutn)


        self.verticalLayout_12.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget2)
        self.label_8.setObjectName(u"label_8")
        sizePolicy2.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy2)
        self.label_8.setFont(font4)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_8)

        self.pushButton_getRestDishes_5 = QPushButton(self.layoutWidget2)
        self.pushButton_getRestDishes_5.setObjectName(u"pushButton_getRestDishes_5")
        self.pushButton_getRestDishes_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(100, 100, 100);\n"
"}")

        self.verticalLayout_7.addWidget(self.pushButton_getRestDishes_5)


        self.verticalLayout_12.addLayout(self.verticalLayout_7)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.layoutWidget2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)
        self.label_2.setFont(font4)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_2)

        self.lineEdit_allRestaurantDishes = QLineEdit(self.layoutWidget2)
        self.lineEdit_allRestaurantDishes.setObjectName(u"lineEdit_allRestaurantDishes")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lineEdit_allRestaurantDishes.sizePolicy().hasHeightForWidth())
        self.lineEdit_allRestaurantDishes.setSizePolicy(sizePolicy3)
        self.lineEdit_allRestaurantDishes.setMinimumSize(QSize(40, 0))
        self.lineEdit_allRestaurantDishes.setMaximumSize(QSize(99999, 16777215))
        font5 = QFont()
        font5.setWeight(QFont.Medium)
        self.lineEdit_allRestaurantDishes.setFont(font5)
        self.lineEdit_allRestaurantDishes.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.lineEdit_allRestaurantDishes.setStyleSheet(u"QLineEdit{\n"
"	margin-bottom: 10px;\n"
"	padding: 3px;\n"
"}")
        self.lineEdit_allRestaurantDishes.setCursorPosition(0)
        self.lineEdit_allRestaurantDishes.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.lineEdit_allRestaurantDishes)

        self.pushButton_getRestDishes = QPushButton(self.layoutWidget2)
        self.pushButton_getRestDishes.setObjectName(u"pushButton_getRestDishes")
        self.pushButton_getRestDishes.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(120, 120, 120);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 5px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"	padding: 4px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(100, 100, 100);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_getRestDishes)


        self.verticalLayout_12.addLayout(self.verticalLayout_3)


        self.horizontalLayout_13.addLayout(self.verticalLayout_12)

        self.label_18 = QLabel(self.page_home)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(340, 100, 351, 61))
        font6 = QFont()
        font6.setPointSize(14)
        font6.setBold(False)
        font6.setItalic(True)
        self.label_18.setFont(font6)
        self.stackedWidget.addWidget(self.page_home)
        self.page_usuarios = QWidget()
        self.page_usuarios.setObjectName(u"page_usuarios")
        self.tabla_users = QTableWidget(self.page_usuarios)
        if (self.tabla_users.columnCount() < 7):
            self.tabla_users.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tabla_users.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tabla_users.setObjectName(u"tabla_users")
        self.tabla_users.setGeometry(QRect(20, 160, 990, 551))
        self.tabla_users.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QTableWidget::item, QTableView::item {\n"
"    background-color: #FFFFFF; \n"
"}\n"
"\n"
"QTableWidget::item:alternate, QTableView::item:alternate {\n"
"    background-color: #F2F2F2; \n"
"}")
        self.tabla_users.setAlternatingRowColors(True)
        self.tabla_users.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tabla_users.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_users.setColumnCount(7)
        self.tabla_users.horizontalHeader().setVisible(True)
        self.tabla_users.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_users.horizontalHeader().setDefaultSectionSize(120)
        self.tabla_users.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_users.horizontalHeader().setStretchLastSection(True)
        self.tabla_users.verticalHeader().setVisible(False)
        self.tabla_users.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_users.verticalHeader().setStretchLastSection(False)
        self.lineEdit_search_email = QLineEdit(self.page_usuarios)
        self.lineEdit_search_email.setObjectName(u"lineEdit_search_email")
        self.lineEdit_search_email.setGeometry(QRect(740, 110, 271, 35))
        self.lineEdit_search_email.setMinimumSize(QSize(0, 35))
        self.lineEdit_search_email.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_search_email.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.users_management = QLabel(self.page_usuarios)
        self.users_management.setObjectName(u"users_management")
        self.users_management.setGeometry(QRect(20, 50, 221, 41))
        font7 = QFont()
        font7.setFamilies([u"Segoe UI"])
        font7.setPointSize(13)
        self.users_management.setFont(font7)
        self.users_tittle = QLabel(self.page_usuarios)
        self.users_tittle.setObjectName(u"users_tittle")
        self.users_tittle.setGeometry(QRect(20, 0, 121, 51))
        self.users_tittle.setFont(font)
        self.layoutWidget3 = QWidget(self.page_usuarios)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 100, 271, 42))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.btn_addUser_2 = QPushButton(self.layoutWidget3)
        self.btn_addUser_2.setObjectName(u"btn_addUser_2")
        self.btn_addUser_2.setMinimumSize(QSize(0, 40))
        self.btn_addUser_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_addUser_2)

        self.btn_exportToPDF = QPushButton(self.layoutWidget3)
        self.btn_exportToPDF.setObjectName(u"btn_exportToPDF")
        self.btn_exportToPDF.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 56, 56); \n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_2.addWidget(self.btn_exportToPDF)

        self.stackedWidget.addWidget(self.page_usuarios)
        self.page_restaurantes = QWidget()
        self.page_restaurantes.setObjectName(u"page_restaurantes")
        self.tabla_restaurants = QTableWidget(self.page_restaurantes)
        if (self.tabla_restaurants.columnCount() < 8):
            self.tabla_restaurants.setColumnCount(8)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_restaurants.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        self.tabla_restaurants.setObjectName(u"tabla_restaurants")
        self.tabla_restaurants.setGeometry(QRect(20, 160, 990, 541))
        self.tabla_restaurants.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QTableWidget::item, QTableView::item {\n"
"    background-color: #FFFFFF; \n"
"}\n"
"\n"
"QTableWidget::item:alternate, QTableView::item:alternate {\n"
"    background-color: #F2F2F2; \n"
"}")
        self.tabla_restaurants.setAlternatingRowColors(True)
        self.tabla_restaurants.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tabla_restaurants.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_restaurants.setColumnCount(8)
        self.tabla_restaurants.horizontalHeader().setVisible(True)
        self.tabla_restaurants.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_restaurants.horizontalHeader().setDefaultSectionSize(110)
        self.tabla_restaurants.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_restaurants.horizontalHeader().setStretchLastSection(True)
        self.tabla_restaurants.verticalHeader().setVisible(False)
        self.tabla_restaurants.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_restaurants.verticalHeader().setStretchLastSection(False)
        self.lineEdit_searchByNameCategoryTlfn = QLineEdit(self.page_restaurantes)
        self.lineEdit_searchByNameCategoryTlfn.setObjectName(u"lineEdit_searchByNameCategoryTlfn")
        self.lineEdit_searchByNameCategoryTlfn.setGeometry(QRect(740, 110, 271, 35))
        self.lineEdit_searchByNameCategoryTlfn.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchByNameCategoryTlfn.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchByNameCategoryTlfn.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.restaurant_management = QLabel(self.page_restaurantes)
        self.restaurant_management.setObjectName(u"restaurant_management")
        self.restaurant_management.setGeometry(QRect(20, 50, 261, 41))
        self.restaurant_management.setFont(font2)
        self.layoutWidget_2 = QWidget(self.page_restaurantes)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 100, 271, 42))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.btn_addRestaurant = QPushButton(self.layoutWidget_2)
        self.btn_addRestaurant.setObjectName(u"btn_addRestaurant")
        self.btn_addRestaurant.setMinimumSize(QSize(0, 40))
        self.btn_addRestaurant.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_addRestaurant)

        self.btn_exportToPDF_5 = QPushButton(self.layoutWidget_2)
        self.btn_exportToPDF_5.setObjectName(u"btn_exportToPDF_5")
        self.btn_exportToPDF_5.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF_5.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 56, 56); \n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_6.addWidget(self.btn_exportToPDF_5)

        self.restaurant_tittle = QLabel(self.page_restaurantes)
        self.restaurant_tittle.setObjectName(u"restaurant_tittle")
        self.restaurant_tittle.setGeometry(QRect(20, 0, 241, 51))
        self.restaurant_tittle.setFont(font3)
        self.stackedWidget.addWidget(self.page_restaurantes)
        self.page_platos = QWidget()
        self.page_platos.setObjectName(u"page_platos")
        self.tabla_plates = QTableWidget(self.page_platos)
        if (self.tabla_plates.columnCount() < 6):
            self.tabla_plates.setColumnCount(6)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(0, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(1, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(2, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(3, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(4, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_plates.setHorizontalHeaderItem(5, __qtablewidgetitem20)
        self.tabla_plates.setObjectName(u"tabla_plates")
        self.tabla_plates.setGeometry(QRect(20, 160, 990, 551))
        self.tabla_plates.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QTableWidget::item, QTableView::item {\n"
"    background-color: #FFFFFF; \n"
"}\n"
"\n"
"QTableWidget::item:alternate, QTableView::item:alternate {\n"
"    background-color: #F2F2F2; \n"
"}")
        self.tabla_plates.setAlternatingRowColors(True)
        self.tabla_plates.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tabla_plates.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_plates.setColumnCount(6)
        self.tabla_plates.horizontalHeader().setVisible(True)
        self.tabla_plates.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_plates.horizontalHeader().setDefaultSectionSize(165)
        self.tabla_plates.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_plates.horizontalHeader().setStretchLastSection(True)
        self.tabla_plates.verticalHeader().setVisible(False)
        self.tabla_plates.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_plates.verticalHeader().setStretchLastSection(False)
        self.lineEdit_searchByNameDescription = QLineEdit(self.page_platos)
        self.lineEdit_searchByNameDescription.setObjectName(u"lineEdit_searchByNameDescription")
        self.lineEdit_searchByNameDescription.setGeometry(QRect(740, 110, 271, 35))
        self.lineEdit_searchByNameDescription.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchByNameDescription.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchByNameDescription.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.plates_tittle = QLabel(self.page_platos)
        self.plates_tittle.setObjectName(u"plates_tittle")
        self.plates_tittle.setGeometry(QRect(20, 0, 241, 51))
        self.plates_tittle.setFont(font3)
        self.layoutWidget_3 = QWidget(self.page_platos)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(20, 100, 271, 42))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_7.setSpacing(10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.btn_addPlate = QPushButton(self.layoutWidget_3)
        self.btn_addPlate.setObjectName(u"btn_addPlate")
        self.btn_addPlate.setMinimumSize(QSize(0, 40))
        self.btn_addPlate.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_addPlate)

        self.btn_exportToPDF_2 = QPushButton(self.layoutWidget_3)
        self.btn_exportToPDF_2.setObjectName(u"btn_exportToPDF_2")
        self.btn_exportToPDF_2.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF_2.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 56, 56); \n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_7.addWidget(self.btn_exportToPDF_2)

        self.plates_management = QLabel(self.page_platos)
        self.plates_management.setObjectName(u"plates_management")
        self.plates_management.setGeometry(QRect(20, 50, 261, 41))
        self.plates_management.setFont(font2)
        self.stackedWidget.addWidget(self.page_platos)
        self.page_pedidos = QWidget()
        self.page_pedidos.setObjectName(u"page_pedidos")
        self.tabla_orders = QTableWidget(self.page_pedidos)
        if (self.tabla_orders.columnCount() < 5):
            self.tabla_orders.setColumnCount(5)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tabla_orders.setHorizontalHeaderItem(4, __qtablewidgetitem25)
        self.tabla_orders.setObjectName(u"tabla_orders")
        self.tabla_orders.setGeometry(QRect(20, 160, 990, 551))
        self.tabla_orders.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QTableWidget::item, QTableView::item {\n"
"    background-color: #FFFFFF; \n"
"}\n"
"\n"
"QTableWidget::item:alternate, QTableView::item:alternate {\n"
"    background-color: #F2F2F2; \n"
"}")
        self.tabla_orders.setAlternatingRowColors(True)
        self.tabla_orders.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tabla_orders.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_orders.setColumnCount(5)
        self.tabla_orders.horizontalHeader().setVisible(True)
        self.tabla_orders.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_orders.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_orders.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_orders.horizontalHeader().setStretchLastSection(True)
        self.tabla_orders.verticalHeader().setVisible(False)
        self.tabla_orders.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_orders.verticalHeader().setStretchLastSection(False)
        self.lineEdit_searchByUserID = QLineEdit(self.page_pedidos)
        self.lineEdit_searchByUserID.setObjectName(u"lineEdit_searchByUserID")
        self.lineEdit_searchByUserID.setGeometry(QRect(740, 110, 271, 35))
        self.lineEdit_searchByUserID.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchByUserID.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchByUserID.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.plates_management_2 = QLabel(self.page_pedidos)
        self.plates_management_2.setObjectName(u"plates_management_2")
        self.plates_management_2.setGeometry(QRect(20, 50, 261, 41))
        self.plates_management_2.setFont(font2)
        self.plates_tittle_2 = QLabel(self.page_pedidos)
        self.plates_tittle_2.setObjectName(u"plates_tittle_2")
        self.plates_tittle_2.setGeometry(QRect(20, 0, 241, 51))
        self.plates_tittle_2.setFont(font3)
        self.layoutWidget_4 = QWidget(self.page_pedidos)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(20, 100, 271, 42))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_8.setSpacing(10)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.btn_addOrder = QPushButton(self.layoutWidget_4)
        self.btn_addOrder.setObjectName(u"btn_addOrder")
        self.btn_addOrder.setMinimumSize(QSize(0, 40))
        self.btn_addOrder.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_addOrder)

        self.btn_exportToPDF_3 = QPushButton(self.layoutWidget_4)
        self.btn_exportToPDF_3.setObjectName(u"btn_exportToPDF_3")
        self.btn_exportToPDF_3.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF_3.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 56, 56); \n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_8.addWidget(self.btn_exportToPDF_3)

        self.stackedWidget.addWidget(self.page_pedidos)
        self.page_detallesPedidos = QWidget()
        self.page_detallesPedidos.setObjectName(u"page_detallesPedidos")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.page_detallesPedidos.sizePolicy().hasHeightForWidth())
        self.page_detallesPedidos.setSizePolicy(sizePolicy4)
        self.plates_management_3 = QLabel(self.page_detallesPedidos)
        self.plates_management_3.setObjectName(u"plates_management_3")
        self.plates_management_3.setGeometry(QRect(20, 50, 261, 41))
        self.plates_management_3.setFont(font2)
        self.layoutWidget_5 = QWidget(self.page_detallesPedidos)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(20, 100, 321, 42))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.btn_addOrderDetails = QPushButton(self.layoutWidget_5)
        self.btn_addOrderDetails.setObjectName(u"btn_addOrderDetails")
        self.btn_addOrderDetails.setMinimumSize(QSize(0, 40))
        self.btn_addOrderDetails.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_addOrderDetails)

        self.btn_exportToPDF_4 = QPushButton(self.layoutWidget_5)
        self.btn_exportToPDF_4.setObjectName(u"btn_exportToPDF_4")
        self.btn_exportToPDF_4.setMinimumSize(QSize(0, 40))
        self.btn_exportToPDF_4.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 56, 56); \n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout_9.addWidget(self.btn_exportToPDF_4)

        self.plates_tittle_3 = QLabel(self.page_detallesPedidos)
        self.plates_tittle_3.setObjectName(u"plates_tittle_3")
        self.plates_tittle_3.setGeometry(QRect(20, 0, 281, 51))
        self.plates_tittle_3.setFont(font3)
        self.lineEdit_searchByOrderID = QLineEdit(self.page_detallesPedidos)
        self.lineEdit_searchByOrderID.setObjectName(u"lineEdit_searchByOrderID")
        self.lineEdit_searchByOrderID.setGeometry(QRect(740, 110, 271, 35))
        self.lineEdit_searchByOrderID.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchByOrderID.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchByOrderID.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.tabla_ordersDetails = QTableWidget(self.page_detallesPedidos)
        if (self.tabla_ordersDetails.columnCount() < 5):
            self.tabla_ordersDetails.setColumnCount(5)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tabla_ordersDetails.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        self.tabla_ordersDetails.setObjectName(u"tabla_ordersDetails")
        self.tabla_ordersDetails.setGeometry(QRect(20, 160, 990, 551))
        sizePolicy1.setHeightForWidth(self.tabla_ordersDetails.sizePolicy().hasHeightForWidth())
        self.tabla_ordersDetails.setSizePolicy(sizePolicy1)
        self.tabla_ordersDetails.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QTableWidget::item, QTableView::item {\n"
"    background-color: #FFFFFF; \n"
"}\n"
"\n"
"QTableWidget::item:alternate, QTableView::item:alternate {\n"
"    background-color: #F2F2F2; \n"
"}")
        self.tabla_ordersDetails.setAlternatingRowColors(True)
        self.tabla_ordersDetails.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tabla_ordersDetails.setTextElideMode(Qt.TextElideMode.ElideMiddle)
        self.tabla_ordersDetails.setColumnCount(5)
        self.tabla_ordersDetails.horizontalHeader().setVisible(True)
        self.tabla_ordersDetails.horizontalHeader().setCascadingSectionResizes(False)
        self.tabla_ordersDetails.horizontalHeader().setDefaultSectionSize(200)
        self.tabla_ordersDetails.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_ordersDetails.horizontalHeader().setStretchLastSection(True)
        self.tabla_ordersDetails.verticalHeader().setVisible(False)
        self.tabla_ordersDetails.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_ordersDetails.verticalHeader().setStretchLastSection(False)
        self.stackedWidget.addWidget(self.page_detallesPedidos)
        self.page_repartidores = QWidget()
        self.page_repartidores.setObjectName(u"page_repartidores")
        self.label_3 = QLabel(self.page_repartidores)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 0, 311, 51))
        self.label_3.setFont(font3)
        self.label_4 = QLabel(self.page_repartidores)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 50, 281, 41))
        self.label_4.setFont(font2)
        self.tabla_delivery = QTableWidget(self.page_repartidores)
        if (self.tabla_delivery.columnCount() < 6):
            self.tabla_delivery.setColumnCount(6)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(1, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(4, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tabla_delivery.setHorizontalHeaderItem(5, __qtablewidgetitem36)
        self.tabla_delivery.setObjectName(u"tabla_delivery")
        self.tabla_delivery.setGeometry(QRect(20, 160, 990, 551))
        self.tabla_delivery.setMinimumSize(QSize(0, 0))
        self.tabla_delivery.setStyleSheet(u"QHeaderView::section{\n"
"	font-weight: bold;\n"
"	background-color: black;\n"
"	color: white;\n"
"}\n"
"\n"
"QTableWidget{\n"
"	alternate-background-color: #B0EDFB;\n"
"	background-color: #FFFFFF;\n"
"}\n"
"\n"
"QTableWidget::item, QTableView::item {\n"
"    background-color: #FFFFFF; \n"
"}\n"
"\n"
"QTableWidget::item:alternate, QTableView::item:alternate {\n"
"    background-color: #F2F2F2; \n"
"}")
        self.tabla_delivery.setAutoScrollMargin(16)
        self.tabla_delivery.setAlternatingRowColors(True)
        self.tabla_delivery.setSelectionMode(QAbstractItemView.SelectionMode.NoSelection)
        self.tabla_delivery.setShowGrid(True)
        self.tabla_delivery.setWordWrap(True)
        self.tabla_delivery.setCornerButtonEnabled(True)
        self.tabla_delivery.setColumnCount(6)
        self.tabla_delivery.horizontalHeader().setVisible(True)
        self.tabla_delivery.horizontalHeader().setCascadingSectionResizes(True)
        self.tabla_delivery.horizontalHeader().setMinimumSectionSize(32)
        self.tabla_delivery.horizontalHeader().setDefaultSectionSize(160)
        self.tabla_delivery.horizontalHeader().setHighlightSections(True)
        self.tabla_delivery.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tabla_delivery.horizontalHeader().setStretchLastSection(True)
        self.tabla_delivery.verticalHeader().setVisible(False)
        self.tabla_delivery.verticalHeader().setCascadingSectionResizes(False)
        self.tabla_delivery.verticalHeader().setHighlightSections(True)
        self.tabla_delivery.verticalHeader().setStretchLastSection(False)
        self.lineEdit_searchBy = QLineEdit(self.page_repartidores)
        self.lineEdit_searchBy.setObjectName(u"lineEdit_searchBy")
        self.lineEdit_searchBy.setGeometry(QRect(740, 110, 271, 35))
        self.lineEdit_searchBy.setMinimumSize(QSize(0, 35))
        self.lineEdit_searchBy.setMaximumSize(QSize(16777215, 35))
        self.lineEdit_searchBy.setStyleSheet(u"QLineEdit{\n"
"	padding-left: 10px;\n"
"	border: 1px solid gray;\n"
"	border-radius: 10px;\n"
"}\n"
"")
        self.layoutWidget_6 = QWidget(self.page_repartidores)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(20, 100, 271, 42))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_addDelivery = QPushButton(self.layoutWidget_6)
        self.btn_addDelivery.setObjectName(u"btn_addDelivery")
        self.btn_addDelivery.setMinimumSize(QSize(0, 40))
        self.btn_addDelivery.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(0, 0, 0);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(50, 50, 50);\n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout.addWidget(self.btn_addDelivery)

        self.btn_exportPDF = QPushButton(self.layoutWidget_6)
        self.btn_exportPDF.setObjectName(u"btn_exportPDF")
        self.btn_exportPDF.setMinimumSize(QSize(0, 40))
        self.btn_exportPDF.setStyleSheet(u"QPushButton{\n"
"	\n"
"	background-color: rgb(218, 29, 29);\n"
"	color: white;\n"
"	border: none;\n"
"	border-radius: 8px;\n"
"	font-weight: bold;\n"
"	font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(255, 56, 56); \n"
"    cursor: pointer; \n"
"}")

        self.horizontalLayout.addWidget(self.btn_exportPDF)

        self.stackedWidget.addWidget(self.page_repartidores)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Just Meat App", None))
        self.label.setText("")
        self.btn_reports.setText("")
        self.btn_querys.setText("")
        self.btn_users.setText("")
        self.btn_restaurants.setText("")
        self.btn_dishes.setText("")
        self.btn_delivery.setText("")
        self.btn_orders.setText("")
        self.btn_orderDetails.setText("")
        self.users_tittle_2.setText(QCoreApplication.translate("MainWindow", u"Querys", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Top-rated restaurants and their most expensive dishes ", None))
        self.pushButton_q1.setText(QCoreApplication.translate("MainWindow", u"Get ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Users with the most orders and their favorite restaurant", None))
        self.pushButton_q2.setText(QCoreApplication.translate("MainWindow", u"Get ", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Delivery driver performance by order status", None))
        self.pushButton_q3.setText(QCoreApplication.translate("MainWindow", u"Get ", None))
        self.pushButton_q4.setText(QCoreApplication.translate("MainWindow", u"Get ", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Most popular dishes by restaurant category", None))
        self.pushButton_q5.setText(QCoreApplication.translate("MainWindow", u"Get ", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Customers never ordered from Italian categ", None))
        self.pushButton_q6.setText(QCoreApplication.translate("MainWindow", u"Get ", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Restaurants with pending orders", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Reports Management Area", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Reports ", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Cross-Analysis of Users, Dishes and Categories", None))
        self.pushButton_crossAnalysis.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Top 5 Restaurants by Sales Volume", None))
        self.pushButton_getTopRestaurants.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Customer Analysis and Consumption Habits", None))
        self.pushButton_getConsum.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Analysis of Dish Popularity and Profitability", None))
        self.pushButton_getbutn.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Restaurant Efficiency Analysis by Order Status", None))
        self.pushButton_getRestDishes_5.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"User Orders History", None))
        self.lineEdit_allRestaurantDishes.setPlaceholderText(QCoreApplication.translate("MainWindow", u"User ID...", None))
        self.pushButton_getRestDishes.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"All Reports will be saved in ''Reports\" folder", None))
        ___qtablewidgetitem = self.tabla_users.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tabla_users.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem2 = self.tabla_users.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem3 = self.tabla_users.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem4 = self.tabla_users.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem5 = self.tabla_users.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"CreationDate", None));
        ___qtablewidgetitem6 = self.tabla_users.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Items", None));
        self.lineEdit_search_email.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by username or email...", None))
        self.users_management.setText(QCoreApplication.translate("MainWindow", u"Users management area", None))
        self.users_tittle.setText(QCoreApplication.translate("MainWindow", u"Users", None))
        self.btn_addUser_2.setText(QCoreApplication.translate("MainWindow", u"Add User", None))
        self.btn_exportToPDF.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        ___qtablewidgetitem7 = self.tabla_restaurants.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem8 = self.tabla_restaurants.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem9 = self.tabla_restaurants.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem10 = self.tabla_restaurants.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem11 = self.tabla_restaurants.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem12 = self.tabla_restaurants.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Schedule", None));
        ___qtablewidgetitem13 = self.tabla_restaurants.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Qualification", None));
        ___qtablewidgetitem14 = self.tabla_restaurants.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Items", None));
        self.lineEdit_searchByNameCategoryTlfn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by name, phone, category...", None))
        self.restaurant_management.setText(QCoreApplication.translate("MainWindow", u"Restaurants management area", None))
        self.btn_addRestaurant.setText(QCoreApplication.translate("MainWindow", u"Add Restaurant", None))
        self.btn_exportToPDF_5.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.restaurant_tittle.setText(QCoreApplication.translate("MainWindow", u"Restaurants", None))
        ___qtablewidgetitem15 = self.tabla_plates.horizontalHeaderItem(0)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem16 = self.tabla_plates.horizontalHeaderItem(1)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem17 = self.tabla_plates.horizontalHeaderItem(2)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem18 = self.tabla_plates.horizontalHeaderItem(3)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem19 = self.tabla_plates.horizontalHeaderItem(4)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Restaurant ID", None));
        ___qtablewidgetitem20 = self.tabla_plates.horizontalHeaderItem(5)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Items", None));
        self.lineEdit_searchByNameDescription.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by name, description ...", None))
        self.plates_tittle.setText(QCoreApplication.translate("MainWindow", u"Plates", None))
        self.btn_addPlate.setText(QCoreApplication.translate("MainWindow", u"Add Plate", None))
        self.btn_exportToPDF_2.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.plates_management.setText(QCoreApplication.translate("MainWindow", u"Plates management area", None))
        ___qtablewidgetitem21 = self.tabla_orders.horizontalHeaderItem(0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem22 = self.tabla_orders.horizontalHeaderItem(1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"User ID", None));
        ___qtablewidgetitem23 = self.tabla_orders.horizontalHeaderItem(2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Restaurant ID", None));
        ___qtablewidgetitem24 = self.tabla_orders.horizontalHeaderItem(3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"State", None));
        ___qtablewidgetitem25 = self.tabla_orders.horizontalHeaderItem(4)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Items", None));
        self.lineEdit_searchByUserID.setText("")
        self.lineEdit_searchByUserID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by UserID ...", None))
        self.plates_management_2.setText(QCoreApplication.translate("MainWindow", u"Orders management area", None))
        self.plates_tittle_2.setText(QCoreApplication.translate("MainWindow", u"Orders", None))
        self.btn_addOrder.setText(QCoreApplication.translate("MainWindow", u"Add Order", None))
        self.btn_exportToPDF_3.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.plates_management_3.setText(QCoreApplication.translate("MainWindow", u"Orders details management area", None))
        self.btn_addOrderDetails.setText(QCoreApplication.translate("MainWindow", u"Add Order Details", None))
        self.btn_exportToPDF_4.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
        self.plates_tittle_3.setText(QCoreApplication.translate("MainWindow", u"Orders Details", None))
        self.lineEdit_searchByOrderID.setText("")
        self.lineEdit_searchByOrderID.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by OrderID ...", None))
        ___qtablewidgetitem26 = self.tabla_ordersDetails.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem27 = self.tabla_ordersDetails.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Order ID", None));
        ___qtablewidgetitem28 = self.tabla_ordersDetails.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Plate ID", None));
        ___qtablewidgetitem29 = self.tabla_ordersDetails.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem30 = self.tabla_ordersDetails.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Items", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Delivery People", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Delivery People management area", None))
        ___qtablewidgetitem31 = self.tabla_delivery.horizontalHeaderItem(0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem32 = self.tabla_delivery.horizontalHeaderItem(1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"NIF", None));
        ___qtablewidgetitem33 = self.tabla_delivery.horizontalHeaderItem(2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem34 = self.tabla_delivery.horizontalHeaderItem(3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Order ID", None));
        ___qtablewidgetitem35 = self.tabla_delivery.horizontalHeaderItem(4)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Vehicle", None));
        ___qtablewidgetitem36 = self.tabla_delivery.horizontalHeaderItem(5)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Items", None));
        self.lineEdit_searchBy.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search by NIF, name ...", None))
        self.btn_addDelivery.setText(QCoreApplication.translate("MainWindow", u"Add Delivery", None))
        self.btn_exportPDF.setText(QCoreApplication.translate("MainWindow", u"Export to PDF", None))
    # retranslateUi

