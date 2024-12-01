
import os

class FileSystem:
    def __init__(self):
        self.current_directory = os.getcwd()

    def create_folder(self, folder_name):
    def touch_file(self, file_name):
        with open(file_name, "w") as f:
            f.write("")
        except Exception as e:
            print(f"Error creating file: {e}")
    def create_file(self, file_name):
        with open(file_name, "w") as f:
            f.write("")
        except Exception as e:
            print(f"Error creating file: {e}")
        os.makedirs(folder_name, exist_ok=True)
        except OSError as e:
            print(f"Error: {e}")


def main():
        fs.log_command(cmd)
        fs.log_command(cmd)
    fs = FileSystem()
    while True:
        cmd = input('Enter command: ')
        if cmd.startswith('mkdir'):
            _, folder_name = cmd.split()
            fs.create_folder(folder_name)
        elif cmd == 'exit':
            break

if __name__ == '__main__':
    main()


    def list_directory(self):
        contents = os.listdir(self.current_directory)
        for item in contents:
            print(item)


    def list_directory(self):
        contents = os.listdir(self.current_directory)
        for item in contents:
            print(item)


    def list_directory(self):
        contents = os.listdir(self.current_directory)
        for item in contents:
            print(item)


    def change_directory(self, directory_name):
        try:
            os.chdir(directory_name)
            self.current_directory = os.getcwd()
            print(fChanged directory to {self.current_directory})
        except FileNotFoundError:
            print(Directory does not exist.)


import logging

logging.basicConfig(filename='fs_emulator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class FileSystem:
    ...
    def log_command(self, command):
        logging.info(command)


import logging

logging.basicConfig(filename='fs_emulator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class FileSystem:
    ...
    def log_command(self, command):
        logging.info(command)


    def print_working_directory(self):
        print(self.current_directory)


    def remove_file(self, file_name):
        try:
            os.remove(file_name)
            print(fFile {file_name} removed successfully.)
        except FileNotFoundError:
            print(File not found.)
        except OSError as e:
            print(fError removing file: {e})


    def remove_file(self, file_name):
        try:
            os.remove(file_name)
            print(fFile {file_name} removed successfully.)
        except FileNotFoundError:
            print(File not found.)
        except OSError as e:
            print(fError removing file: {e})


    def remove_file(self, file_name):
        try:
            os.remove(file_name)
            print(fFile {file_name} removed successfully.)
        except FileNotFoundError:
            print(File not found.)
        except OSError as e:
            print(fError removing file: {e})


    def display_tree(self, path=None, prefix=''):
        if path is None:
            path = self.current_directory

        contents = os.listdir(path)
        for i, item in enumerate(contents):
            connector = '└── ' if i == len(contents) - 1 else '├── '
            print(f{prefix}{connector}{item})
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                self.display_tree(item_path, prefix + ('    ' if i == len(contents) - 1 else '│   '))

