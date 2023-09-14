# This Python file uses the following encoding: utf-8
import sys

from PySide6.QtWidgets import QApplication, QMainWindow,QFileDialog

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_path=''
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
    def connection(self):
        self.ui.browserFile.clicked.connect(self.get_browser_show)

    def get_browser_show(self):
       self.file_path =QFileDialog.getOpenFileName(self,"Select File","c:\\")
       self.ui.pathEdit.setText(self.file_path[0])
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.connection()
    widget.show()
    sys.exit(app.exec())
