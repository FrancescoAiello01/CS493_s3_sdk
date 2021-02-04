from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QComboBox, QFileDialog, QGridLayout, QLabel, QMessageBox, QPushButton, QWidget, QLineEdit
from models.s3_connector import S3Connector
import os


class MusicScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.grid_layout = QGridLayout(self)
        self.init_ui()
        self.s3_connector = S3Connector()

    def init_ui(self):
        self.create_aws_profile_specification()
        self.create_bucket_dropdown()
        self.create_single_file_upload()
        self.create_directory_file_upload()
        
        
    def create_directory_file_upload(self):
        select_directory_label = QLabel("Select a directory for upload")
        self.input_directory_field = QLineEdit()
        self.select_directory_button = QPushButton("...")
        self.select_directory_button.clicked.connect(self.select_directory_listener)
        
        self.upload_directory_button = QPushButton("upload to s3")
        self.upload_directory_button.clicked.connect(self.upload_directory_listener)
        
        aws_directory_name_label = QLabel("Rename directory (if desired)")
        self.aws_directory_name = QLineEdit()
        
        self.grid_layout.addWidget(select_directory_label, 4, 0)
        self.grid_layout.addWidget(self.input_directory_field, 4, 1)
        self.grid_layout.addWidget(self.select_directory_button, 4, 2)
        
        self.grid_layout.addWidget(aws_directory_name_label, 5, 1)
        self.grid_layout.addWidget(self.aws_directory_name, 5, 2)
        self.grid_layout.addWidget(self.upload_directory_button, 5, 3)
        
    def select_directory_listener(self):
        directory_name = QFileDialog.getExistingDirectory(parent=self, caption='Select directory')
        if directory_name:
            self.input_directory_field.setText(directory_name)
            self.aws_directory_name.setText(os.path.basename(directory_name))
            
    def upload_directory_listener(self):
        path = self.input_directory_field.text()
        directory_name = self.aws_directory_name.text()
        bucket = str(self.bucket_dropdown.currentText())
        self.s3_connector.upload_directory(directory_path=path,
                                      bucket_name=bucket, aws_directory=directory_name)
        self.success_message_box("Upload Confirmation", 'Successfully uploaded to S3!')
        
        
    def create_single_file_upload(self):
        select_file_label = QLabel("Select a file for upload")
        self.input_file_field = QLineEdit()
        self.select_file_button = QPushButton("...")
        self.select_file_button.clicked.connect(self.select_file_listener)
        
        self.upload_file_button = QPushButton("upload to s3")
        self.upload_file_button.clicked.connect(self.upload_file_listener)
        
        aws_file_name_label = QLabel("Rename file (if desired)")
        self.aws_file_name = QLineEdit()
        
        self.grid_layout.addWidget(select_file_label, 2, 0)
        self.grid_layout.addWidget(self.input_file_field, 2, 1)
        self.grid_layout.addWidget(self.select_file_button, 2, 2)
        
        self.grid_layout.addWidget(aws_file_name_label, 3, 1)
        self.grid_layout.addWidget(self.aws_file_name, 3, 2)
        self.grid_layout.addWidget(self.upload_file_button, 3, 3)
        
    def upload_file_listener(self):
        path = self.input_file_field.text()
        file_name = self.aws_file_name.text()
        bucket = str(self.bucket_dropdown.currentText())
        self.s3_connector.upload_file(
            file_path=path, file_name=file_name, bucket_name=bucket)
        self.success_message_box("Upload Confirmation", 'Successfully uploaded to S3!')
        
    def success_message_box(self, title, message):
        self.status_message_box = QMessageBox()
        self.status_message_box.setIcon(QMessageBox.Information)
        self.status_message_box.setText(message)
        self.status_message_box.setWindowTitle(title)
        self.status_message_box.setStandardButtons(QMessageBox.Ok)
        self.status_message_box.show()
        
    def select_file_listener(self):
        filename, filter = QFileDialog.getOpenFileName(parent=self, caption='Open file')
        if filename:
            self.input_file_field.setText(filename)
            self.aws_file_name.setText(os.path.basename(filename))

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
        