# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
                               QLineEdit, QListWidget, QListWidgetItem, QMainWindow,
                               QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import files_rc


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(705, 500)
        MainWindow.setMinimumSize(QSize(300, 500))
        icon = QIcon()
        icon.addFile(u":/icons/icons/calculator.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QWidget {\n"
                                 "                color: white;\n"
                                 "                background-color: #121212;\n"
                                 "                font-family: Rubik;\n"
                                 "                font-size: 16pt;\n"
                                 "                font-weight: 600;\n"
                                 "                }\n"
                                 "\n"
                                 "                QPushButton {\n"
                                 "                background-color: transparent;\n"
                                 "                border: none;\n"
                                 "                }\n"
                                 "\n"
                                 "                QPushButton:hover {\n"
                                 "                background-color: #666;\n"
                                 "                }\n"
                                 "\n"
                                 "                QPushButton:pressed {\n"
                                 "                background-color: #888;\n"
                                 "                }\n"
                                 "            ")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.list_methods = QListWidget(self.centralwidget)
        self.list_methods.setObjectName(u"list_methods")

        self.verticalLayout.addWidget(self.list_methods)

        self.layout_edit_input = QHBoxLayout()
        self.layout_edit_input.setObjectName(u"layout_edit_input")
        self.layout_text_input = QVBoxLayout()
        self.layout_text_input.setObjectName(u"layout_text_input")
        self.text_input_1 = QLineEdit(self.centralwidget)
        self.text_input_1.setObjectName(u"text_input_1")

        self.layout_text_input.addWidget(self.text_input_1)

        self.text_input_2 = QLineEdit(self.centralwidget)
        self.text_input_2.setObjectName(u"text_input_2")

        self.layout_text_input.addWidget(self.text_input_2)

        self.layout_edit_input.addLayout(self.layout_text_input)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.le_input_1 = QLineEdit(self.centralwidget)
        self.le_input_1.setObjectName(u"le_input_1")

        self.verticalLayout_2.addWidget(self.le_input_1)

        self.le_input_2 = QLineEdit(self.centralwidget)
        self.le_input_2.setObjectName(u"le_input_2")

        self.verticalLayout_2.addWidget(self.le_input_2)

        self.layout_edit_input.addLayout(self.verticalLayout_2)

        self.layout_edit_input.setStretch(0, 1)
        self.layout_edit_input.setStretch(1, 6)

        self.verticalLayout.addLayout(self.layout_edit_input)

        self.layout_output = QHBoxLayout()
        self.layout_output.setObjectName(u"layout_output")
        self.le_entry = QLineEdit(self.centralwidget)
        self.le_entry.setObjectName(u"le_entry")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.le_entry.sizePolicy().hasHeightForWidth())
        self.le_entry.setSizePolicy(sizePolicy)
        self.le_entry.setStyleSheet(u"font-size: 40pt;\n"
                                    "                                border: none;\n"
                                    "                            ")
        self.le_entry.setMaxLength(16)
        self.le_entry.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.le_entry.setReadOnly(True)

        self.layout_output.addWidget(self.le_entry)

        self.img_grafic = QLabel(self.centralwidget)
        self.img_grafic.setObjectName(u"img_grafic")

        self.layout_output.addWidget(self.img_grafic)

        self.verticalLayout.addLayout(self.layout_output)

        self.lbl_temp = QLabel(self.centralwidget)
        self.lbl_temp.setObjectName(u"lbl_temp")
        self.lbl_temp.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_temp.sizePolicy().hasHeightForWidth())
        self.lbl_temp.setSizePolicy(sizePolicy1)
        self.lbl_temp.setStyleSheet(u"color: #888;")
        self.lbl_temp.setAlignment(Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)

        self.verticalLayout.addWidget(self.lbl_temp)

        self.layout_buttons = QGridLayout()
        self.layout_buttons.setObjectName(u"layout_buttons")
        self.btn_4 = QPushButton(self.centralwidget)
        self.btn_4.setObjectName(u"btn_4")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btn_4.sizePolicy().hasHeightForWidth())
        self.btn_4.setSizePolicy(sizePolicy2)
        self.btn_4.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_4, 2, 0, 1, 1)

        self.btn_0 = QPushButton(self.centralwidget)
        self.btn_0.setObjectName(u"btn_0")
        sizePolicy2.setHeightForWidth(self.btn_0.sizePolicy().hasHeightForWidth())
        self.btn_0.setSizePolicy(sizePolicy2)
        self.btn_0.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_0, 4, 1, 1, 1)

        self.btn_sub = QPushButton(self.centralwidget)
        self.btn_sub.setObjectName(u"btn_sub")
        sizePolicy2.setHeightForWidth(self.btn_sub.sizePolicy().hasHeightForWidth())
        self.btn_sub.setSizePolicy(sizePolicy2)
        self.btn_sub.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_sub, 2, 3, 1, 1)

        self.btn_backspace = QPushButton(self.centralwidget)
        self.btn_backspace.setObjectName(u"btn_backspace")
        sizePolicy2.setHeightForWidth(self.btn_backspace.sizePolicy().hasHeightForWidth())
        self.btn_backspace.setSizePolicy(sizePolicy2)
        self.btn_backspace.setCursor(QCursor(Qt.PointingHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/backspace.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_backspace.setIcon(icon1)
        self.btn_backspace.setIconSize(QSize(24, 24))

        self.layout_buttons.addWidget(self.btn_backspace, 0, 2, 1, 1)

        self.btn_clear = QPushButton(self.centralwidget)
        self.btn_clear.setObjectName(u"btn_clear")
        sizePolicy2.setHeightForWidth(self.btn_clear.sizePolicy().hasHeightForWidth())
        self.btn_clear.setSizePolicy(sizePolicy2)
        self.btn_clear.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_clear, 0, 0, 1, 1)

        self.btn_point = QPushButton(self.centralwidget)
        self.btn_point.setObjectName(u"btn_point")
        sizePolicy2.setHeightForWidth(self.btn_point.sizePolicy().hasHeightForWidth())
        self.btn_point.setSizePolicy(sizePolicy2)
        self.btn_point.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_point, 4, 2, 1, 1)

        self.btn_7 = QPushButton(self.centralwidget)
        self.btn_7.setObjectName(u"btn_7")
        sizePolicy2.setHeightForWidth(self.btn_7.sizePolicy().hasHeightForWidth())
        self.btn_7.setSizePolicy(sizePolicy2)
        self.btn_7.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_7, 1, 0, 1, 1)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        sizePolicy2.setHeightForWidth(self.btn_add.sizePolicy().hasHeightForWidth())
        self.btn_add.setSizePolicy(sizePolicy2)
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_add, 3, 3, 1, 1)

        self.btn_6 = QPushButton(self.centralwidget)
        self.btn_6.setObjectName(u"btn_6")
        sizePolicy2.setHeightForWidth(self.btn_6.sizePolicy().hasHeightForWidth())
        self.btn_6.setSizePolicy(sizePolicy2)
        self.btn_6.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_6, 2, 2, 1, 1)

        self.btn_ce = QPushButton(self.centralwidget)
        self.btn_ce.setObjectName(u"btn_ce")
        sizePolicy2.setHeightForWidth(self.btn_ce.sizePolicy().hasHeightForWidth())
        self.btn_ce.setSizePolicy(sizePolicy2)
        self.btn_ce.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_ce, 0, 1, 1, 1)

        self.btn_calc = QPushButton(self.centralwidget)
        self.btn_calc.setObjectName(u"btn_calc")
        sizePolicy2.setHeightForWidth(self.btn_calc.sizePolicy().hasHeightForWidth())
        self.btn_calc.setSizePolicy(sizePolicy2)
        self.btn_calc.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_calc, 4, 3, 1, 1)

        self.btn_1 = QPushButton(self.centralwidget)
        self.btn_1.setObjectName(u"btn_1")
        sizePolicy2.setHeightForWidth(self.btn_1.sizePolicy().hasHeightForWidth())
        self.btn_1.setSizePolicy(sizePolicy2)
        self.btn_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_1, 3, 0, 1, 1)

        self.btn_neg = QPushButton(self.centralwidget)
        self.btn_neg.setObjectName(u"btn_neg")
        sizePolicy2.setHeightForWidth(self.btn_neg.sizePolicy().hasHeightForWidth())
        self.btn_neg.setSizePolicy(sizePolicy2)
        self.btn_neg.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_neg, 4, 0, 1, 1)

        self.btn_div = QPushButton(self.centralwidget)
        self.btn_div.setObjectName(u"btn_div")
        sizePolicy2.setHeightForWidth(self.btn_div.sizePolicy().hasHeightForWidth())
        self.btn_div.setSizePolicy(sizePolicy2)
        self.btn_div.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_div, 0, 3, 1, 1)

        self.btn_mul = QPushButton(self.centralwidget)
        self.btn_mul.setObjectName(u"btn_mul")
        sizePolicy2.setHeightForWidth(self.btn_mul.sizePolicy().hasHeightForWidth())
        self.btn_mul.setSizePolicy(sizePolicy2)
        self.btn_mul.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_mul, 1, 3, 1, 1)

        self.btn_5 = QPushButton(self.centralwidget)
        self.btn_5.setObjectName(u"btn_5")
        sizePolicy2.setHeightForWidth(self.btn_5.sizePolicy().hasHeightForWidth())
        self.btn_5.setSizePolicy(sizePolicy2)
        self.btn_5.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_5, 2, 1, 1, 1)

        self.btn_3 = QPushButton(self.centralwidget)
        self.btn_3.setObjectName(u"btn_3")
        sizePolicy2.setHeightForWidth(self.btn_3.sizePolicy().hasHeightForWidth())
        self.btn_3.setSizePolicy(sizePolicy2)
        self.btn_3.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_3, 3, 2, 1, 1)

        self.btn_9 = QPushButton(self.centralwidget)
        self.btn_9.setObjectName(u"btn_9")
        sizePolicy2.setHeightForWidth(self.btn_9.sizePolicy().hasHeightForWidth())
        self.btn_9.setSizePolicy(sizePolicy2)
        self.btn_9.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_9, 1, 2, 1, 1)

        self.btn_8 = QPushButton(self.centralwidget)
        self.btn_8.setObjectName(u"btn_8")
        sizePolicy2.setHeightForWidth(self.btn_8.sizePolicy().hasHeightForWidth())
        self.btn_8.setSizePolicy(sizePolicy2)
        self.btn_8.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_8, 1, 1, 1, 1)

        self.btn_2 = QPushButton(self.centralwidget)
        self.btn_2.setObjectName(u"btn_2")
        sizePolicy2.setHeightForWidth(self.btn_2.sizePolicy().hasHeightForWidth())
        self.btn_2.setSizePolicy(sizePolicy2)
        self.btn_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.layout_buttons.addWidget(self.btn_2, 3, 1, 1, 1)

        self.verticalLayout.addLayout(self.layout_buttons)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"shtosh calculator", None))
        self.le_entry.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.img_grafic.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        # if QT_CONFIG(shortcut)
        self.btn_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        # if QT_CONFIG(shortcut)
        self.btn_0.setShortcut(QCoreApplication.translate("MainWindow", u"0", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_sub.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
        # if QT_CONFIG(shortcut)
        self.btn_sub.setShortcut(QCoreApplication.translate("MainWindow", u"-", None))
        # endif // QT_CONFIG(shortcut)
        # if QT_CONFIG(shortcut)
        self.btn_backspace.setShortcut(QCoreApplication.translate("MainWindow", u"Backspace", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_clear.setText(QCoreApplication.translate("MainWindow", u"C", None))
        self.btn_point.setText(QCoreApplication.translate("MainWindow", u".", None))
        # if QT_CONFIG(shortcut)
        self.btn_point.setShortcut(QCoreApplication.translate("MainWindow", u".", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"+", None))
        # if QT_CONFIG(shortcut)
        self.btn_add.setShortcut(QCoreApplication.translate("MainWindow", u"+", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        # if QT_CONFIG(shortcut)
        self.btn_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_ce.setText(QCoreApplication.translate("MainWindow", u"CE", None))
        # if QT_CONFIG(shortcut)
        self.btn_ce.setShortcut(QCoreApplication.translate("MainWindow", u"Del", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_calc.setText(QCoreApplication.translate("MainWindow", u"=", None))
        # if QT_CONFIG(shortcut)
        self.btn_calc.setShortcut(QCoreApplication.translate("MainWindow", u"=", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        # if QT_CONFIG(shortcut)
        self.btn_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_neg.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.btn_div.setText(QCoreApplication.translate("MainWindow", u"/", None))
        # if QT_CONFIG(shortcut)
        self.btn_div.setShortcut(QCoreApplication.translate("MainWindow", u"/", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_mul.setText(QCoreApplication.translate("MainWindow", u"\u00d7", None))
        # if QT_CONFIG(shortcut)
        self.btn_mul.setShortcut(QCoreApplication.translate("MainWindow", u"*", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        # if QT_CONFIG(shortcut)
        self.btn_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        # if QT_CONFIG(shortcut)
        self.btn_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
        # endif // QT_CONFIG(shortcut)
        self.btn_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.btn_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.btn_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        # if QT_CONFIG(shortcut)
        self.btn_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
# endif // QT_CONFIG(shortcut)
# retranslateUi