from PyQt5.QtWidgets import QApplication, QMainWindow, QTabWidget, QWidget, QVBoxLayout, QLabel

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create a QTabWidget
        self.tabs = QTabWidget()
        self.setCentralWidget(self.tabs)

        # Create the widgets for each tab
        tab1 = QWidget()
        label1 = QLabel("This is tab 1")
        layout1 = QVBoxLayout(tab1)
        layout1.addWidget(label1)

        tab2 = QWidget()
        label2 = QLabel("This is tab 2")
        layout2 = QVBoxLayout(tab2)
        layout2.addWidget(label2)

        tab3 = QWidget()
        label3 = QLabel("This is tab 3")
        layout3 = QVBoxLayout(tab3)
        layout3.addWidget(label3)

        tab4 = QWidget()
        label4 = QLabel('This is tab 4')
        layout4 = QVBoxLayout(tab4)
        layout4.addWidget(label4)

        # Add the tabs to the QTabWidget
        self.tabs.addTab(tab1, "Chat (playground)")
        self.tabs.addTab(tab2, "Complete (playground)")
        self.tabs.addTab(tab3, "Prompt Generator")
        self.tabs.addTab(tab4, "Image Generator")


if __name__ == '__main__':
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
