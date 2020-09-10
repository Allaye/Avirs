from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets, QtGui


class helpwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Avirs Help')
        self.setGeometry(450, 350, 150, 600)
        self.ui()

    def ui(self):
        self.show()

class mainwin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Qmenu')
        self.setGeometry(340, 340, 360, 700)
        self.ui()

    def ui(self):
        self.mainMenu = self.menuBar()
        self.project = QLabel()
        self.fileMenu = self.mainMenu.addMenu('File')
        self.fileMenu.addAction('Add File')
        self.help = self.mainMenu.addMenu('Help')
        self.help.aboutToShow.connect(self.helpwindow)

        # self.fileMenu.triggered.connect(self.loadImageFromFile)

    def helpwindow(self):
        self.newwin = helpwindow()
        self.close()


def main():
    app = QApplication([])
    win = mainwin()
    win.show()
    app.exec()


if __name__ == "__main__":
    main()
