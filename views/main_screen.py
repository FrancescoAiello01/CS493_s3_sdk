from PyQt5.QtWidgets import QMainWindow
from views.music_screen import MusicScreen


class MainScreen(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        width = 500
        height = 500
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        self.music_screen = MusicScreen()
        self.setCentralWidget(self.music_screen)
