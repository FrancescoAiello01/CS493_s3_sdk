from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QComboBox, QGridLayout, QLabel, QPushButton, QWidget, QLineEdit
from models.s3_connector import S3Connector


class MusicScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.init_ui()
        self.s3_connector = S3Connector()

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
        buckets = self.s3_connector.get_buckets()
        self.bucket_dropdown.addItems(buckets)
    
    def create_aws_profile_specification(self):
        aws_profile_label = QLabel("AWS Profile (leave blank for default)")
        self.aws_profile = QLineEdit()
        save_button = QPushButton("Save")
        save_button.clicked.connect(self.update_aws_profile)
        
        self.grid_layout.addWidget(aws_profile_label, 0, 0)
        self.grid_layout.addWidget(self.aws_profile, 0, 1)
        self.grid_layout.addWidget(save_button, 0, 2)
        
    def update_aws_profile(self):
        if self.aws_profile.text():
            self.s3_connector.connect(self.aws_profile.text())
        else:
            self.s3_connector.connect('default')
        