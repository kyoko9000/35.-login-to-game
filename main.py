import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication, QMainWindow
from gui import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)

        self.uic.Button_log_in.clicked.connect(self.login_game)
        self.uic.Button_sign_in.clicked.connect(self.sign_in)

    def sign_in(self):
        # read id and password on sign in
        s_id = self.uic.screen_id_2.text()
        s_password = self.uic.screen_password_2.text()

        # write string to file
        lines = [s_id, s_password]
        with open('life.txt', 'a') as f:
            for line in lines:
                f.write(line)
                f.write('\n')

    def login_game(self):
        # read file text
        my_file = open("life.txt", "r")
        content = my_file.read()
        print(content)
        # make list of index in text file
        content_1 = content.split("\n")
        my_file.close()
        print(content_1)

        # remove last empty index
        content_list = content_1[:-1]
        print(content_list)

        # separate index in to 2 list: id and password
        ID_list = content_list[0::2]
        print("id list", ID_list)
        Password_list = content_list[1::2]
        print("password list", Password_list)

        # input id
        input_id = self.uic.screen_id_1.text()
        try:
            # find index in list
            index = ID_list.index(input_id)
            s_password = Password_list[index]
            print(index, s_password)

            # input password
            input_password = self.uic.screen_password_1.text()
            if input_password != s_password:
                print("sai password")
            if input_password == s_password:
                self.close()
                from DoAn1 import start_menu
                start_menu()
        except:
            print("sai id")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())