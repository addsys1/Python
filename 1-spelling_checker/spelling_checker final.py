
# pyuic5 main.ui -o main_ui.py

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import sys
from PyQt5 import QtWidgets
from textblob import TextBlob
from main_ui import Ui_MainWindow



class Main(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(Main,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.setWindowTitle("SpellCheckPlus")
        self.setFixedSize(746, 368)  # Set fixed width and height
        self.Handel_Buttons()
        
    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.spell_check)
        self.pushButton_2.clicked.connect(self.clear)

    def spell_check(self):
        input = TextBlob(self.textEdit.toPlainText())
        output = input.correct()
        
        self.textEdit_2.setText(str(output))
    
    
    def clear(self):
        self.textEdit.setText('')
        self.textEdit_2.setText('')
         


def main():
    app = QApplication(sys.argv)
    window = Main()
    window.show()
    app.exec_()

if '__main__' ==__name__:
    main()