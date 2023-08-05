from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QPushButton

class CustomizeDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initVal()
        self.__initUi()

    def __initVal(self):
        pass

    def __initUi(self):
        self.setWindowTitle('Customize (working)')
        self.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set the window flags to keep the main window always on top
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        # Set the main window geometry (x, y, width, height)
        self.setGeometry(300, 300, 400, 200)

        # Create a button to open a dialog window
        self.button = QPushButton('Open Dialog', self)
        self.button.clicked.connect(self.openDialog)

        # Set the button geometry (x, y, width, height)
        self.button.setGeometry(150, 80, 100, 40)

    def openDialog(self):
        # Create a dialog window with the main window as its parent
        dialog = CustomizeDialog(self)
        dialog.exec_()


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
