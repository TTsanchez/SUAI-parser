from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from parsing import *
from styles import *
import os.path
import datetime


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        MainWindow.setFocusPolicy(QtCore.Qt.ClickFocus)

        if os.path.isfile("favicon.svg"):
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap("favicon.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            MainWindow.setWindowIcon(icon)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(MainWindowStyle)
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setAnimated(True)
        MainWindow.setDocumentMode(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        MainWindow.setUnifiedTitleAndToolBarOnMac(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)


        self.centralwidget.setObjectName("centralwidget")

        ######################## poisk_form ########################
        self.poisk_form = QtWidgets.QLineEdit(self.centralwidget)
        self.poisk_form.setEnabled(True)
        self.poisk_form.setGeometry(QtCore.QRect(300, 55, 200, 42))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(16)
        self.poisk_form.setFont(font)
        self.poisk_form.setTabletTracking(False)
        self.poisk_form.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.poisk_form.setContextMenuPolicy(Qt.NoContextMenu)
        self.poisk_form.setAcceptDrops(True)
        self.poisk_form.setStatusTip("")
        self.poisk_form.setAccessibleName("")
        self.poisk_form.setAutoFillBackground(False)
        self.poisk_form.setStyleSheet(poisk_formStyle)
        self.poisk_form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.poisk_form.setInputMask("")
        self.poisk_form.setText("")
        self.poisk_form.setMaxLength(10)
        self.poisk_form.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.poisk_form.setAlignment(QtCore.Qt.AlignCenter)
        self.poisk_form.setDragEnabled(False)
        self.poisk_form.setClearButtonEnabled(False)
        self.poisk_form.setObjectName("poisk_form")
        ########################### END ###########################


        ########################## label ##########################
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(200, 10, 400, 42))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setMouseTracking(False)
        self.label.setFocusPolicy(QtCore.Qt.TabFocus)
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(labelStyle)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        ########################### END ###########################

        ########################## Pr_Bar ##########################
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setEnabled(True)
        self.progressBar.setGeometry(QtCore.QRect(300, 55, 200, 42))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.progressBar.sizePolicy().hasHeightForWidth())
        self.progressBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.progressBar.setFont(font)
        self.progressBar.setAcceptDrops(False)
        self.progressBar.setToolTip("")
        self.progressBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.progressBar.setAutoFillBackground(False)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(False)
        self.progressBar.setInvertedAppearance(False)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.setStyleSheet(ProgressBarStyle)
        self.progressBar.hide()
        ########################### END ###########################


        ##################### str_under_poisk #####################
        self.str_under_poisk = QtWidgets.QLabel(self.centralwidget)
        self.str_under_poisk.setGeometry(QtCore.QRect(0, 105, 800, 38))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.str_under_poisk.setFont(font)
        self.str_under_poisk.setStyleSheet(str_under_poiskStyle)
        self.str_under_poisk.setAlignment(QtCore.Qt.AlignCenter)
        self.str_under_poisk.setObjectName("str_under_poisk")
        ########################### END ###########################

        ##################### str_types_of_weeks #####################
        self.str_types_of_weeks = QtWidgets.QLabel(self.centralwidget)
        self.str_types_of_weeks.setGeometry(QtCore.QRect(0, 125, 800, 38))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.str_types_of_weeks.setFont(font)
        self.str_types_of_weeks.setStyleSheet(str_types_of_weeksStyle)
        self.str_types_of_weeks.setAlignment(QtCore.Qt.AlignCenter)
        self.str_types_of_weeks.setObjectName("str_types_of_weeks")
        ########################### END ###########################


        ######################### textEdit ########################
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setEnabled(True)
        self.textEdit.setReadOnly(True)
        self.textEdit.setGeometry(QtCore.QRect(5, 155, 795, 450))
        font = QtGui.QFont()
        font.setFamily("Roboto Medium")
        font.setPointSize(13)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(TextEditStyle)
        self.textEdit.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.textEdit.setObjectName("textEdit")
        ########################### END ###########################


        ######################## MenuButton #######################
        self.MenuButton = QtWidgets.QPushButton(self.centralwidget)
        self.MenuButton.setGeometry(QtCore.QRect(15, 15, 32, 32))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MenuButton.setFont(font)
        self.MenuButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        if os.path.isfile("images/menu.png") and os.path.isfile("images/menu_hover.png") and os.path.isfile(
                "images/menu_pressed.png"):
            self.MenuButton.setStyleSheet(MenuButtonStyle)
            self.menu_img = True
        else:
            self.MenuButton.setStyleSheet(MenuButtonStyleLite)
            self.menu_img = False
        self.MenuButton.setCheckable(False)
        self.MenuButton.setObjectName("MenuButton")
        ########################### END ###########################


        ########################### Frame ###########################
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(250, 200, 300, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet(FrameStyle)
        self.frame.hide()
        ########################### END ###########################

        ####################### HeadingMenu #######################
        self.HeadingMenu = QtWidgets.QLabel(self.frame)
        self.HeadingMenu.setGeometry(QtCore.QRect(0, 0, 300, 32))
        font = QtGui.QFont()
        font.setFamily("Roboto Black")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.HeadingMenu.setFont(font)
        self.HeadingMenu.setMouseTracking(False)
        # self.HeadingMenu.setFocusPolicy(QtCore.Qt.TabFocus)
        self.HeadingMenu.setAutoFillBackground(False)
        self.HeadingMenu.setStyleSheet(labelStyle)
        self.HeadingMenu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.HeadingMenu.setFrameShadow(QtWidgets.QFrame.Plain)
        self.HeadingMenu.setScaledContents(False)
        self.HeadingMenu.setAlignment(QtCore.Qt.AlignCenter)
        self.HeadingMenu.setWordWrap(False)
        self.HeadingMenu.setText('Меню')
        self.HeadingMenu.setEnabled(False)
        self.HeadingMenu.setObjectName("HeadingMenu")
        ########################### END ###########################

        ######################### Buttons #########################
        self.CloseButton = QtWidgets.QPushButton(self.frame)
        self.CloseButton.setGeometry(QtCore.QRect(268, 0, 32, 32))
        self.CloseButton.setObjectName("CloseButton")
        if os.path.isfile("images/close.png") and os.path.isfile("images/close_hover.png") and os.path.isfile(
                "images/close_pressed.png"):
            self.CloseButton.setStyleSheet(CloseButtonStyle)
            self.CloseButton_Img = True
        else:
            self.CloseButton.setStyleSheet(CloseButtonStyleLite)
            self.CloseButton_Img = False
        self.Search_GP_Button = QtWidgets.QPushButton(self.frame)
        self.Search_GP_Button.setGeometry(QtCore.QRect(15, 50, 270, 30))
        self.Search_GP_Button.setObjectName("Search_GP_Button")
        self.Search_GP_Button.setStyleSheet(SearchButtonsStyleActive)
        self.Search_Teach_Button = QtWidgets.QPushButton(self.frame)
        self.Search_Teach_Button.setGeometry(QtCore.QRect(15, 90, 270, 30))
        self.Search_Teach_Button.setObjectName("Search_Teach_Button")
        self.Search_Teach_Button.setStyleSheet(SearchButtonsStyle)
        self.Search_AU_Button = QtWidgets.QPushButton(self.frame)
        self.Search_AU_Button.setGeometry(QtCore.QRect(15, 130, 270, 30))
        self.Search_AU_Button.setObjectName("Search_AU_Button")
        self.Search_AU_Button.setStyleSheet(SearchButtonsStyle)
        ########################### END ###########################
        self.search = "GP"
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.poisk_form.returnPressed.connect(self.progressBar.show)  # Pr_Bar
        self.poisk_form.returnPressed.connect(self.plotBarChart)
        self.poisk_form.returnPressed.connect(self.poisk_form.clear) # type: ignore

        self.MenuButton.clicked.connect(self.click_menu)  # type: ignore
        self.CloseButton.clicked.connect(self.click_exit_frame)
        self.Search_GP_Button.clicked.connect(lambda:self.click_s_gp())
        self.Search_Teach_Button.clicked.connect(lambda: self.click_s_teach())
        self.Search_AU_Button.clicked.connect(lambda: self.click_s_au())


        #QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SUAI Parser"))
        self.poisk_form.setPlaceholderText(_translate("MainWindow", "Номер группы"))
        self.label.setText(_translate("MainWindow", "Найти расписание группы"))
        self.progressBar.setFormat(_translate("MainWindow", "%p%"))
        self.str_under_poisk.setText(_translate("MainWindow", ""))
        self.textEdit.setHtml(_translate("MainWindow", ""))
        self.MenuButton.setText(_translate("MainWindow", ""))
        self.CloseButton.setText(_translate("MainWindow", ""))
        self.Search_GP_Button.setText(_translate("MainWindow", "Поиск по номеру группы"))
        self.Search_Teach_Button.setText(_translate("MainWindow", "Поиск по преподавателю"))
        self.Search_AU_Button.setText(_translate("MainWindow", "Поиск по аудитории"))

        #Если не найдены картинки кнопок
        if self.menu_img == False:
            self.MenuButton.setText(_translate("MainWindow", "≡"))
        if self.CloseButton_Img == False:
            self.CloseButton.setText(_translate("MainWindow", "×"))

    def plotBarChart(self):
        QApplication.setOverrideCursor(Qt.WaitCursor) # ставится курсор загрузки
        form_out = str(self.poisk_form.text()).title().strip()
        print(form_out)
        if (form_out == "" or checking(form_out) == -1) or \
                (self.search == "Teach" and checking_without_num(form_out) == -1):
            print("Некорректный ввод")
            self.str_under_poisk.setText("Некорректный ввод")
            self.progressBar.hide()  # Pr_Bar
            QApplication.restoreOverrideCursor() # возвращается обычный курсор
            return
        resp_val, week = parser(form_out, self)
        if resp_val == 0:
            print("Не найдено")
            self.str_under_poisk.setText("Не найдено")
            QApplication.restoreOverrideCursor()
        elif resp_val == -1:
            print("Нет интернет соединения")
            self.str_under_poisk.setText("Нет интернет соединения")
            QApplication.restoreOverrideCursor()
        elif resp_val == -2:
            print("Некорректный ввод")
            self.str_under_poisk.setText("Некорректный ввод")
            QApplication.restoreOverrideCursor()
        else:
            print(resp_val)
            if self.search == "GP":
                self.str_under_poisk.setText("Расписание для группы - " + form_out)
            elif self.search == "Teach":
                self.str_under_poisk.setText("Расписание для преподавателя - " + form_out)
            elif self.search == "AU":
                self.str_under_poisk.setText("Расписание для ауд. - " + form_out)
            if week == 'четная':
                self.str_types_of_weeks.setText(OddWeekStyle)
            else:
                self.str_types_of_weeks.setText(EvenWeekStyle)
            self.textEdit.setStyleSheet(TextEditStyle2)
            self.textEdit.setText(resp_val)
        self.progressBar.setValue(0)
        self.progressBar.hide()  # скрыть Progress bar
        QApplication.restoreOverrideCursor()

        value = self.textEdit.verticalScrollBar().value()  # позиция слайдера
        week = ['Понедельник',
                'Вторник',
                'Среда',
                'Четверг',
                'Пятница',
                'Суббота',
                'Воскресенье']
        weekDay = week[datetime.datetime.today().weekday()]
        print(weekDay, datetime.datetime.today().weekday())
        self.textEdit.find(weekDay)
        if self.textEdit.verticalScrollBar().value() > 0:
            self.textEdit.verticalScrollBar().setValue(self.textEdit.verticalScrollBar().value() + 420)

    def click_menu(self):
        self.frame.show()
        self.poisk_form.setEnabled(False)
        self.MenuButton.setEnabled(False)
        self.textEdit.setEnabled(False)

    def click_exit_frame(self):
        self.frame.hide()
        self.poisk_form.setEnabled(True)
        self.MenuButton.setEnabled(True)
        self.textEdit.setEnabled(True)

    def click_s_gp(self):
        self.Search_GP_Button.setStyleSheet(SearchButtonsStyleActive)
        self.Search_Teach_Button.setStyleSheet(SearchButtonsStyle)
        self.Search_AU_Button.setStyleSheet(SearchButtonsStyle)
        self.poisk_form.setGeometry(QtCore.QRect(300, 55, 200, 42))
        self.progressBar.setGeometry(QtCore.QRect(300, 55, 200, 42))
        self.poisk_form.setPlaceholderText("Номер группы")
        self.poisk_form.setMaxLength(10)
        self.label.setText("Найти расписание группы")
        self.search = "GP"

    def click_s_teach(self):
        self.Search_GP_Button.setStyleSheet(SearchButtonsStyle)
        self.Search_Teach_Button.setStyleSheet(SearchButtonsStyleActive)
        self.Search_AU_Button.setStyleSheet(SearchButtonsStyle)
        self.poisk_form.setGeometry(QtCore.QRect(275, 55, 250, 42))
        self.progressBar.setGeometry(QtCore.QRect(275, 55, 250, 42))
        self.poisk_form.setPlaceholderText("Иванов И.И.")
        self.poisk_form.setMaxLength(19)
        self.label.setText("Найти расписание преподавателя")
        self.search = "Teach"

    def click_s_au(self):
        self.Search_GP_Button.setStyleSheet(SearchButtonsStyle)
        self.Search_Teach_Button.setStyleSheet(SearchButtonsStyle)
        self.Search_AU_Button.setStyleSheet(SearchButtonsStyleActive)
        self.poisk_form.setGeometry(QtCore.QRect(300, 55, 200, 42))
        self.progressBar.setGeometry(QtCore.QRect(300, 55, 200, 42))
        self.poisk_form.setPlaceholderText("11-11")
        self.poisk_form.setMaxLength(10)
        self.label.setText("Найти расписание по аудитории")
        self.search = "AU"


def checking(stroke):
    exceptions = ['!', '"', '№', ';', '%', '?', '(', ')', '_', '=', '+',
                  '\\', '/', ',', '@', '#','$', '^', '&', '[', ']', '{', '}', "'", '|', '>', "<", "`"]
    for i in exceptions:
        if stroke.find(i) != -1:
            return -1

def checking_without_num(stroke):
    exceptions = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for i in exceptions:
        if stroke.find(i) != -1:
            return -1

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet(QScrollBarStyle)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())