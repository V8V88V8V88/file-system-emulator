
import os

class FileSystem:
    def __init__(self):
        self.current_directory = os.getcwd()

    def create_folder(self, folder_name):
        os.makedirs(folder_name, exist_ok=True)

