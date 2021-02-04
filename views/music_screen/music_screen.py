from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QComboBox, QGridLayout, QLabel, QPushButton, QWidget, QLineEdit


class MusicScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.init_ui()

    def init_ui(self):
        self.create_aws_profile_specification()
        self.create_bucket_dropdown()

    def create_bucket_dropdown(self):
        bucket_label = QLabel("S3 Bucket")
        self.bucket_dropdown = QComboBox()
        self.refresh_bucket = QPushButton() 
        self.refresh_bucket.setIcon(QIcon('views/assets/refresh.png'))
        self.refresh_bucket.clicked.connect(self.populate_bucket_dropdown)
        
        self.grid_layout.addWidget(bucket_label, 1, 0)
        self.grid_layout.addWidget(self.bucket_dropdown, 1, 1)
        self.grid_layout.addWidget(self.refresh_bucket, 1, 2) 
  

    def populate_bucket_dropdown(self):
        print("hi")
    
    def create_aws_profile_specification(self):
        aws_profile_label = QLabel("AWS Profile (leave blank for default)")
        self.aws_profile = QLineEdit()
        self.grid_layout.addWidget(aws_profile_label, 0, 0)
        self.grid_layout.addWidget(self.aws_profile, 0, 1)
        