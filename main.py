import sys
from PyQt5.QtWidgets import QApplication
from views.main_screen import MainScreen

app = QApplication([])

main_screen = MainScreen()
main_screen.showMaximized()
sys.exit(app.exec_())