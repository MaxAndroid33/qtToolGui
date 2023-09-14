# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QFormLayout, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QSplitter, QTabWidget, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, -1, -1, -1)
        self.splitter = QSplitter(self.centralwidget)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.splitter.setHandleWidth(1)
        self.splitter.setChildrenCollapsible(False)
        self.menuSide = QWidget(self.splitter)
        self.menuSide.setObjectName(u"menuSide")
        self.menuSide.setMinimumSize(QSize(200, 0))
        self.menuSide.setMaximumSize(QSize(340, 16777215))
        self.menuSide.setStyleSheet(u"#menuSide{\n"
"border: 1px solid red;\n"
"border-radius:20px;\n"
"\n"
"\n"
"}\n"
"")
        self.formLayout = QFormLayout(self.menuSide)
        self.formLayout.setObjectName(u"formLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.menuSide)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 0))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"border:none;")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.formLayout.setLayout(0, QFormLayout.SpanningRole, self.horizontalLayout_3)

        self.filePathLabel = QLabel(self.menuSide)
        self.filePathLabel.setObjectName(u"filePathLabel")
        self.filePathLabel.setMinimumSize(QSize(20, 0))
        self.filePathLabel.setTabletTracking(False)
        self.filePathLabel.setFrameShape(QFrame.NoFrame)
        self.filePathLabel.setScaledContents(False)
        self.filePathLabel.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.filePathLabel)

        self.pathEdit = QLineEdit(self.menuSide)
        self.pathEdit.setObjectName(u"pathEdit")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.pathEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.formLayout.setLayout(6, QFormLayout.LabelRole, self.horizontalLayout)

        self.tabWidget_3 = QTabWidget(self.menuSide)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setTabShape(QTabWidget.Rounded)
        self.tabWidget_3.setElideMode(Qt.ElideNone)
        self.Tab_7 = QWidget()
        self.Tab_7.setObjectName(u"Tab_7")
        self.formLayout_9 = QFormLayout(self.Tab_7)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.value1Label_3 = QLabel(self.Tab_7)
        self.value1Label_3.setObjectName(u"value1Label_3")

        self.formLayout_9.setWidget(0, QFormLayout.LabelRole, self.value1Label_3)

        self.value1DoubleSpinBox_9 = QDoubleSpinBox(self.Tab_7)
        self.value1DoubleSpinBox_9.setObjectName(u"value1DoubleSpinBox_9")
        self.value1DoubleSpinBox_9.setDecimals(5)
        self.value1DoubleSpinBox_9.setMaximum(10000.000000000000000)

        self.formLayout_9.setWidget(0, QFormLayout.FieldRole, self.value1DoubleSpinBox_9)

        self.value2Label_7 = QLabel(self.Tab_7)
        self.value2Label_7.setObjectName(u"value2Label_7")

        self.formLayout_9.setWidget(1, QFormLayout.LabelRole, self.value2Label_7)

        self.value1DoubleSpinBox_10 = QDoubleSpinBox(self.Tab_7)
        self.value1DoubleSpinBox_10.setObjectName(u"value1DoubleSpinBox_10")
        self.value1DoubleSpinBox_10.setDecimals(5)
        self.value1DoubleSpinBox_10.setMaximum(10000.000000000000000)

        self.formLayout_9.setWidget(1, QFormLayout.FieldRole, self.value1DoubleSpinBox_10)

        self.value2Label_8 = QLabel(self.Tab_7)
        self.value2Label_8.setObjectName(u"value2Label_8")

        self.formLayout_9.setWidget(2, QFormLayout.LabelRole, self.value2Label_8)

        self.value1DoubleSpinBox_11 = QDoubleSpinBox(self.Tab_7)
        self.value1DoubleSpinBox_11.setObjectName(u"value1DoubleSpinBox_11")
        self.value1DoubleSpinBox_11.setDecimals(5)
        self.value1DoubleSpinBox_11.setMaximum(10000.000000000000000)

        self.formLayout_9.setWidget(2, QFormLayout.FieldRole, self.value1DoubleSpinBox_11)

        self.value2Label_9 = QLabel(self.Tab_7)
        self.value2Label_9.setObjectName(u"value2Label_9")

        self.formLayout_9.setWidget(3, QFormLayout.LabelRole, self.value2Label_9)

        self.value1DoubleSpinBox_12 = QDoubleSpinBox(self.Tab_7)
        self.value1DoubleSpinBox_12.setObjectName(u"value1DoubleSpinBox_12")
        self.value1DoubleSpinBox_12.setDecimals(5)
        self.value1DoubleSpinBox_12.setMaximum(10000.000000000000000)

        self.formLayout_9.setWidget(3, QFormLayout.FieldRole, self.value1DoubleSpinBox_12)

        self.tabWidget_3.addTab(self.Tab_7, "")
        self.Tab_8 = QWidget()
        self.Tab_8.setObjectName(u"Tab_8")
        self.Tab_8.setAutoFillBackground(False)
        self.formLayout_10 = QFormLayout(self.Tab_8)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.tabWidget_3.addTab(self.Tab_8, "")
        self.Tab_9 = QWidget()
        self.Tab_9.setObjectName(u"Tab_9")
        self.formLayout_11 = QFormLayout(self.Tab_9)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.tabWidget_3.addTab(self.Tab_9, "")

        self.formLayout.setWidget(2, QFormLayout.SpanningRole, self.tabWidget_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.browserFile = QPushButton(self.menuSide)
        self.browserFile.setObjectName(u"browserFile")

        self.horizontalLayout_2.addWidget(self.browserFile)

        self.pushButton_2 = QPushButton(self.menuSide)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.formLayout.setLayout(5, QFormLayout.SpanningRole, self.horizontalLayout_2)

        self.pushButton = QPushButton(self.menuSide)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(3, QFormLayout.SpanningRole, self.pushButton)

        self.tabWidget_2 = QTabWidget(self.menuSide)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setTabShape(QTabWidget.Rounded)
        self.tabWidget_2.setElideMode(Qt.ElideNone)
        self.Tab_1 = QWidget()
        self.Tab_1.setObjectName(u"Tab_1")
        self.formLayout_3 = QFormLayout(self.Tab_1)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.value1Label = QLabel(self.Tab_1)
        self.value1Label.setObjectName(u"value1Label")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.value1Label)

        self.value1DoubleSpinBox = QDoubleSpinBox(self.Tab_1)
        self.value1DoubleSpinBox.setObjectName(u"value1DoubleSpinBox")
        self.value1DoubleSpinBox.setDecimals(5)
        self.value1DoubleSpinBox.setMaximum(10000.000000000000000)

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.value1DoubleSpinBox)

        self.value2Label = QLabel(self.Tab_1)
        self.value2Label.setObjectName(u"value2Label")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.value2Label)

        self.value1DoubleSpinBox_2 = QDoubleSpinBox(self.Tab_1)
        self.value1DoubleSpinBox_2.setObjectName(u"value1DoubleSpinBox_2")
        self.value1DoubleSpinBox_2.setDecimals(5)
        self.value1DoubleSpinBox_2.setMaximum(10000.000000000000000)

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.value1DoubleSpinBox_2)

        self.value2Label_3 = QLabel(self.Tab_1)
        self.value2Label_3.setObjectName(u"value2Label_3")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.value2Label_3)

        self.value1DoubleSpinBox_4 = QDoubleSpinBox(self.Tab_1)
        self.value1DoubleSpinBox_4.setObjectName(u"value1DoubleSpinBox_4")
        self.value1DoubleSpinBox_4.setDecimals(5)
        self.value1DoubleSpinBox_4.setMaximum(10000.000000000000000)

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.value1DoubleSpinBox_4)

        self.value2Label_2 = QLabel(self.Tab_1)
        self.value2Label_2.setObjectName(u"value2Label_2")

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.value2Label_2)

        self.value1DoubleSpinBox_3 = QDoubleSpinBox(self.Tab_1)
        self.value1DoubleSpinBox_3.setObjectName(u"value1DoubleSpinBox_3")
        self.value1DoubleSpinBox_3.setDecimals(5)
        self.value1DoubleSpinBox_3.setMaximum(10000.000000000000000)

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.value1DoubleSpinBox_3)

        self.tabWidget_2.addTab(self.Tab_1, "")
        self.Tab_2 = QWidget()
        self.Tab_2.setObjectName(u"Tab_2")
        self.Tab_2.setAutoFillBackground(False)
        self.formLayout_4 = QFormLayout(self.Tab_2)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.tabWidget_2.addTab(self.Tab_2, "")
        self.Tab_3 = QWidget()
        self.Tab_3.setObjectName(u"Tab_3")
        self.formLayout_6 = QFormLayout(self.Tab_3)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.tabWidget_2.addTab(self.Tab_3, "")

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.tabWidget_2)

        self.splitter.addWidget(self.menuSide)
        self.tabWidget_2.raise_()
        self.label.raise_()
        self.pathEdit.raise_()
        self.filePathLabel.raise_()
        self.tabWidget_3.raise_()
        self.pushButton_2.raise_()
        self.pushButton.raise_()
        self.browserFile.raise_()
        self.showSide = QWidget(self.splitter)
        self.showSide.setObjectName(u"showSide")
        self.formLayout_2 = QFormLayout(self.showSide)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setHorizontalSpacing(0)
        self.formLayout_2.setVerticalSpacing(0)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.tabWidget = QTabWidget(self.showSide)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.CodeTab = QWidget()
        self.CodeTab.setObjectName(u"CodeTab")
        self.tabWidget.addTab(self.CodeTab, "")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.tabWidget)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetNoConstraint)
        self.verticalLayout.setContentsMargins(0, 0, -1, -1)
        self.menuShow = QPushButton(self.showSide)
        self.menuShow.setObjectName(u"menuShow")
        font1 = QFont()
        font1.setPointSize(13)
        self.menuShow.setFont(font1)
        self.menuShow.setCursor(QCursor(Qt.PointingHandCursor))
        self.menuShow.setAutoFillBackground(False)
        self.menuShow.setStyleSheet(u"border-radius:50px 50px; border:1px solid black;\n"
"\n"
"")
        self.menuShow.setCheckable(True)
        self.menuShow.setChecked(True)
        self.menuShow.setFlat(False)

        self.verticalLayout.addWidget(self.menuShow)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.formLayout_2.setLayout(0, QFormLayout.LabelRole, self.verticalLayout)

        self.splitter.addWidget(self.showSide)

        self.gridLayout.addWidget(self.splitter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menuShow.toggled.connect(self.menuSide.setHidden)
        self.menuShow.toggled.connect(self.menuSide.setVisible)

        self.tabWidget_3.setCurrentIndex(2)
        self.tabWidget_2.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Tools", None))
        self.filePathLabel.setText(QCoreApplication.translate("MainWindow", u"FilePath :", None))
#if QT_CONFIG(accessibility)
        self.tabWidget_3.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.value1Label_3.setText(QCoreApplication.translate("MainWindow", u"value1:", None))
        self.value2Label_7.setText(QCoreApplication.translate("MainWindow", u"value2:", None))
        self.value2Label_8.setText(QCoreApplication.translate("MainWindow", u"value2:", None))
        self.value2Label_9.setText(QCoreApplication.translate("MainWindow", u"value2:", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Tab_7), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Tab_8), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.Tab_9), QCoreApplication.translate("MainWindow", u"Page", None))
        self.browserFile.setText(QCoreApplication.translate("MainWindow", u"Upload File", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Set Values", None))
#if QT_CONFIG(accessibility)
        self.tabWidget_2.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.value1Label.setText(QCoreApplication.translate("MainWindow", u"value1:", None))
        self.value2Label.setText(QCoreApplication.translate("MainWindow", u"value2:", None))
        self.value2Label_3.setText(QCoreApplication.translate("MainWindow", u"value2:", None))
        self.value2Label_2.setText(QCoreApplication.translate("MainWindow", u"value2:", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Tab_1), QCoreApplication.translate("MainWindow", u"vs", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Tab_2), QCoreApplication.translate("MainWindow", u"sds", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.Tab_3), QCoreApplication.translate("MainWindow", u"Page", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Chart", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CodeTab), QCoreApplication.translate("MainWindow", u"Code", None))
        self.menuShow.setText(QCoreApplication.translate("MainWindow", u"T", None))
    # retranslateUi

