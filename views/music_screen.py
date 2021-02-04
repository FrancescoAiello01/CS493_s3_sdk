from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget


class MusicScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.init_ui()

    def init_ui(self):
        test = QLabel("test")
        self.grid_layout.addWidget(test, 2, 3)
