# ======================== Standard and Third-Party Imports =========================
import webbrowser
from PyQt5 import QtCore, QtWidgets
import sys, os, time
import database as db
from PyQt5.QtGui import QIcon
from CustomMessageBox import CustomMessageBox
# ====================================================================================

print("login")

# ============================ Main Window Class Definition ==========================
class Ui_self(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_self, self).__init__()
        self.setupUi()

    # ============================ UI Setup Function =============================
    def setupUi(self):
        self.setWindowIcon(QIcon('icons/nova_no_bg.png'))

        # Automatically open main app if config file exists
        if os.path.exists("user_config.txt"):
            self.open_main()       

        # ---------- Main Window Properties ----------
        self.setObjectName("self")
        self.resize(900, 650)
        self.setMinimumSize(QtCore.QSize(900, 650))
        self.setMaximumSize(QtCore.QSize(900, 650))
        self.setStyleSheet("background-color:#0F1C25;")

        # ---------- Central Widget ----------
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # ---------- Stacked Widget (Pages Container) ----------
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(100, 70, 681, 521))
        self.stackedWidget.setObjectName("stackedWidget")

        # ---------- Sign Up Page ----------
        self.page_signup = QtWidgets.QWidget()
        self.page_signup.setObjectName("page_signup")
        self.setupSignupPage()
        self.stackedWidget.addWidget(self.page_signup)

        # ---------- Login Page ----------
        self.page_login = QtWidgets.QWidget()
        self.page_login.setObjectName("page_login")
        self.setupLoginPage()
        self.stackedWidget.addWidget(self.page_login)

        # ---------- Set Initial Page ----------
        self.stackedWidget.setCurrentWidget(self.page_signup)

        # ---------- Final Setup ----------
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

        # =================== Event Handlers ===================
        # Buttons
        self.pushButton_signup.clicked.connect(self.signup)
        self.pushButton_login_page.clicked.connect(self.login)

        # Clickable Labels
        self.label_goto_signup.mousePressEvent = self.gotoSignupPage
        self.label_goto_login.mousePressEvent = self.gotoLoginPage

        # Text Field Changes
        self.lineEdit_first_name.textChanged.connect(self.onTextChanged)
        self.lineEdit_last_name.textChanged.connect(self.onTextChanged)
        self.lineEdit_Email.textChanged.connect(self.onPasswordChanged)
        self.lineEdit_password.textChanged.connect(self.onPasswordChanged)
        self.lineEdit_confirm_password.textChanged.connect(self.onPasswordChanged)
        self.lineEdit_login_Email.textChanged.connect(self.onLoginChanged)

        # Radio Buttons
        self.radioButton_male.toggled.connect(self.onGenderSelected)
        self.radioButton_female.toggled.connect(self.onGenderSelected)

    # ============================ Signup Page Setup =============================
    def setupSignupPage(self):
        # ---------- Signup Frame ----------
        self.frame_signup = QtWidgets.QFrame(self.page_signup)
        self.frame_signup.setGeometry(QtCore.QRect(0, 0, 681, 521))
        self.frame_signup.setStyleSheet("border: 5px solid #0085FF;\nborder-radius:10px;\ncolor: white;")
        self.frame_signup.setObjectName("frame_signup")

        # ---------- Input Fields ----------
        self.lineEdit_first_name = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_first_name.setGeometry(QtCore.QRect(60, 80, 261, 41))
        self.lineEdit_first_name.setStyleSheet("border:no;\nborder-bottom: 3px solid #0085FF;\n font-size: 20px;")
        self.lineEdit_first_name.setObjectName("lineEdit_first_name")

        self.lineEdit_last_name = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_last_name.setGeometry(QtCore.QRect(360, 80, 271, 41))
        self.lineEdit_last_name.setStyleSheet("border:no;\nborder-bottom: 3px solid #0085FF;\n font-size: 20px;")
        self.lineEdit_last_name.setObjectName("lineEdit_last_name")

        self.lineEdit_Email = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_Email.setGeometry(QtCore.QRect(60, 170, 531, 41))
        self.lineEdit_Email.setStyleSheet("border:no;\nborder-bottom: 3px solid #0085FF;\n font-size: 20px;")
        self.lineEdit_Email.setObjectName("lineEdit_Email")

        self.lineEdit_password = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_password.setGeometry(QtCore.QRect(60, 260, 531, 41))
        self.lineEdit_password.setStyleSheet("border:no;\nborder-bottom: 3px solid #0085FF;\n font-size: 20px;")
        self.lineEdit_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_password.setObjectName("lineEdit_password")

        self.lineEdit_confirm_password = QtWidgets.QLineEdit(self.frame_signup)
        self.lineEdit_confirm_password.setGeometry(QtCore.QRect(60, 340, 531, 41))
        self.lineEdit_confirm_password.setStyleSheet("border:no;\nborder-bottom: 3px solid #0085FF;\n font-size: 20px;")
        self.lineEdit_confirm_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_confirm_password.setObjectName("lineEdit_confirm_password")

        # ---------- Gender Selection ----------
        self.radioButton_male = QtWidgets.QRadioButton(self.frame_signup)
        self.radioButton_male.setGeometry(QtCore.QRect(190, 410, 95, 20))
        self.radioButton_male.setStyleSheet("border:no;\ncolor:#0085FF;\n font-size: 20px;")
        self.radioButton_male.setChecked(True)
        self.radioButton_male.setObjectName("radioButton_male")

        self.radioButton_female = QtWidgets.QRadioButton(self.frame_signup)
        self.radioButton_female.setGeometry(QtCore.QRect(310, 410, 95, 20))
        self.radioButton_female.setStyleSheet("border:no;\ncolor:#0085FF;\n font-size: 20px;")
        self.radioButton_female.setObjectName("radioButton_female")

        # ---------- Warning Label ----------
        self.label_warning = QtWidgets.QLabel(self.frame_signup)
        self.label_warning.setGeometry(QtCore.QRect(60, 390, 400, 20))
        self.label_warning.setStyleSheet("border:no;\ncolor:red;\n font-size: 15px;")

        # ---------- Signup Button ----------
        self.pushButton_signup = QtWidgets.QPushButton(self.frame_signup)
        self.pushButton_signup.setGeometry(QtCore.QRect(230, 450, 171, 51))
        self.pushButton_signup.setStyleSheet("""
            QPushButton#pushButton_signup{
                font-size: 20px;
                background-color:#0085FF;
                border-radius:20px;
            }
            QPushButton#pushButton_signup:hover{
                background-color:lightblue;
                color:#0085FF;
            }
            QPushButton#pushButton_signup:pressed{
                background-color:#0085FF;
                color:white;
            }""")
        self.pushButton_signup.setObjectName("pushButton_signup")

        # ---------- Redirect Label ----------
        self.label_goto_login = QtWidgets.QLabel(self.frame_signup)
        self.label_goto_login.setGeometry(QtCore.QRect(480, 450, 171, 51))
        self.label_goto_login.setStyleSheet("color: #0085FF;\nfont-size: 16px;\nborder: none;\ntext-decoration: underline;")
        self.label_goto_login.setObjectName("label_goto_login")

    # ============================ Login Page Setup =============================
    def setupLoginPage(self):
        self.frame_login = QtWidgets.QFrame(self.page_login)
        self.frame_login.setGeometry(QtCore.QRect(0, 0, 681, 521))
        self.frame_login.setStyleSheet("border: 5px solid #0085FF;\nborder-radius:10px;\ncolor: white;")
        self.frame_login.setObjectName("frame_login")

        self.lineEdit_login_Email = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_login_Email.setGeometry(QtCore.QRect(60, 140, 531, 41))
        self.lineEdit_login_Email.setStyleSheet("border:no;\nborder-bottom: 3px solid #0085FF;\n font-size: 20px;")
        self.lineEdit_login_Email.setObjectName("lineEdit_login_Email")

        self.lineEdit_login_password = QtWidgets.QLineEdit(self.frame_login)
        self.lineEdit_login_password.setGeometry(QtCore.QRect(60, 230, 531, 41))
        self.lineEdit_login_password.setStyleSheet("border:no;\nborder-bottom: 3px solid #0085FF;\n font-size: 20px;")
        self.lineEdit_login_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_login_password.setObjectName("lineEdit_login_password")

        self.label_warning_login = QtWidgets.QLabel(self.frame_login)
        self.label_warning_login.setGeometry(QtCore.QRect(60, 290, 400, 20))
        self.label_warning_login.setStyleSheet("border:no;\ncolor:red;\n font-size: 15px;")

        self.pushButton_login_page = QtWidgets.QPushButton(self.frame_login)
        self.pushButton_login_page.setGeometry(QtCore.QRect(230, 340, 171, 51))
        self.pushButton_login_page.setStyleSheet("""
            QPushButton#pushButton_login_page{
                font-size: 20px;
                background-color:#0085FF;
                border-radius:20px;
            }
            QPushButton#pushButton_login_page:hover{
                background-color:lightblue;
                color:#0085FF;
            }
            QPushButton#pushButton_login_page:pressed{
                background-color:#0085FF;
                color:white;
            }""")
        self.pushButton_login_page.setObjectName("pushButton_login_page")

        self.label_goto_signup = QtWidgets.QLabel(self.frame_login)
        self.label_goto_signup.setGeometry(QtCore.QRect(480, 340, 171, 51))
        self.label_goto_signup.setStyleSheet("color: #0085FF;\nfont-size: 16px;\nborder: none;\ntext-decoration: underline;")
        self.label_goto_signup.setObjectName("label_goto_signup")

    # ============================ Input Validators =============================
    def onPasswordChanged(self):
        email = self.lineEdit_Email.text()
        password = self.lineEdit_password.text()
        confirm_password = self.lineEdit_confirm_password.text()

        if "@" not in email or ".com" not in email:
            self.label_warning.setText("Invalid email format. Please include '@' and '.com'.")
        elif password != confirm_password:
            self.label_warning.setText("Passwords do not match.")
        else:
            self.label_warning.clear()
            return email, confirm_password

    def onTextChanged(self):
        first_name = self.lineEdit_first_name.text()
        last_name = self.lineEdit_last_name.text()

        if not first_name or not last_name:
            self.label_warning.setText("First name and last name cannot be empty.")
        else:
            self.label_warning.clear()
            return first_name, last_name

    def onLoginChanged(self):
        login_email = self.lineEdit_login_Email.text()
        password = self.lineEdit_login_password.text()

        if "@" not in login_email or ".com" not in login_email:
            self.label_warning_login.setText("Invalid email format. Please include '@' and '.com'.")
        else:
            self.label_warning_login.clear()
            return login_email, password

    def onGenderSelected(self):
        if self.radioButton_male.isChecked():
            return "Male"
        elif self.radioButton_female.isChecked():
            return "Female"

    # ============================ Signup Handler =============================
    def signup(self):
        email, confirm_password = self.onPasswordChanged()
        first_name, last_name = self.onTextChanged()
        gender = self.onGenderSelected()

        result = db.sign_up(email, confirm_password, first_name, last_name, gender)

        if result == 0:
            r = CustomMessageBox.show_message(text="""Welcome to NOVA 
NOVA is your intelligent desktop assistant, designed to seamlessly control your system based on your voice and text commands. Get ready to elevate your productivity and simplify your workflow with cutting-edge AI at your fingertips.
Let NOVA handle the details, so you can focus on what matters!
""", B1="learn More", B2="Launch Nova")
            if r:
                webbrowser.open("https://github.com/Siddiq2772/nova_assistant")
                self.open_main()
            else:
                self.open_main()
        else:
            CustomMessageBox.show_message(text=result, B1='Try Again', B2='none')

    # ============================ Login Handler =============================
    def login(self):
        login_email, password = self.onLoginChanged()
        result = db.log_in(login_email, password)

        if result == 0:
            r = CustomMessageBox.show_message(text="""✅ Login Successful! 
Hello, You're now connected to NOVA. Let's get things done effortlessly.
""", B1="LAUNCH NOVA", B2='none')
            if r:
                self.open_main()
        else:
            CustomMessageBox.show_message(text=result, B1='Try Again', B2='none')

    # ============================ Navigation Helpers =============================
    def gotoSignupPage(self, event):
        self.stackedWidget.setCurrentWidget(self.page_signup)

    def gotoLoginPage(self, event):
        self.stackedWidget.setCurrentWidget(self.page_login)

    # ============================ Text Setup / Translation =============================
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle("NOVA")

        # Signup
        self.lineEdit_first_name.setPlaceholderText(_translate("self", "First Name"))
        self.lineEdit_last_name.setPlaceholderText(_translate("self", "Last Name"))
        self.lineEdit_Email.setPlaceholderText(_translate("self", "Email"))
        self.lineEdit_password.setPlaceholderText(_translate("self", "Password"))
        self.lineEdit_confirm_password.setPlaceholderText(_translate("self", "Confirm Password"))
        self.pushButton_signup.setText(_translate("self", "SIGN UP"))
        self.radioButton_male.setText(_translate("self", "Male"))
        self.radioButton_female.setText(_translate("self", "Female"))
        self.label_goto_login.setText(_translate("self", "Already have an account?"))

        # Login
        self.lineEdit_login_Email.setPlaceholderText(_translate("self", "Email"))
        self.lineEdit_login_password.setPlaceholderText(_translate("self", "Password"))
        self.pushButton_login_page.setText(_translate("self", "LOGIN"))
        self.label_goto_signup.setText(_translate("self", "Don't have an account?"))

    # ============================ Open Main App =============================
    def open_main(self):
        self.close()
        if os.path.exists("maingui.exe"):
            os.system("maingui.exe")
        else:
            os.system("python maingui.py")

# ============================ Main Entrypoint =============================
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_self()
    ui.show()
    sys.exit(app.exec_())