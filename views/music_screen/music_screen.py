from PyQt5.QtWidgets import QGridLayout, QLabel, QWidget, QLineEdit


class MusicScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.init_ui()

    def init_ui(self):
        self.create_aws_profile_specification()

    def populate_bucket_dropdown(self):
        pass
    
    def create_aws_profile_specification(self):
        aws_profile_label = QLabel("AWS Profile (leave blank for default)")
        self.aws_profile = QLineEdit()
        self.grid_layout.addWidget(aws_profile_label, 0, 0)
        self.grid_layout.addWidget(self.aws_profile, 0, 1)
        