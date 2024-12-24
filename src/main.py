import os
import logging
from datetime import datetime

# Set up logging
logging.basicConfig(filename='fs_emulator.log', level=logging.INFO, format='%(asctime)s - %(message)s')

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

    @staticmethod
    def colorize(text, color):
        return f"{color}{text}{Colors.ENDC}"

class FileSystem:
    def __init__(self):
    self.current_directory = os.getcwd()
    print(f"Initialized FileSystem with current directory: {self.current_directory}")

    def create_folder(self, folder_name):
        try:
            os.makedirs(folder_name, exist_ok=True)
            print(f"Folder '{folder_name}' created successfully.")
        except OSError as e:
            print(f"Error: {e}")

    def touch_file(self, file_name):
        try:
            with open(file_name, "w") as f:
                f.write("")
            print(f"File '{file_name}' created successfully.")
        except Exception as e:
            print(f"Error creating file: {e}")

    def list_directory(self):
        contents = os.listdir(self.current_directory)
        for item in contents:
            print(Colors.colorize(item, Colors.OKCYAN) if os.path.isdir(os.path.join(self.current_directory, item)) else Colors.colorize(item, Colors.OKGREEN))

    def change_directory(self, directory_name):
        try:
            os.chdir(directory_name)
            self.current_directory = os.getcwd()
            print(f"Changed directory to {self.current_directory}")
        except FileNotFoundError:
            print("Directory does not exist.")

    def print_working_directory(self):
        print(self.current_directory)

    def remove_file(self, file_name):
        try:
            os.remove(file_name)
            print(f"File '{file_name}' removed successfully.")
        except FileNotFoundError:
            print("File not found.")
        except OSError as e:
            print(f"Error removing file: {e}")

    def display_tree(self, path=None, prefix=''):
        if path is None:
            path = self.current_directory

        contents = os.listdir(path)
        for i, item in enumerate(contents):
            connector = '└── ' if i == len(contents) - 1 else '├── '
            print(f"{prefix}{connector}{item}")
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):
                self.display_tree(item_path, prefix + ('    ' if i == len(contents) - 1 else '│   '))

    def rename(self, old_name, new_name):
        try:
            os.rename(old_name, new_name)
            print(f"Renamed \"{old_name}\" to \"{new_name}\" successfully.")
        except FileNotFoundError:
            print("File or folder not found.")
        except OSError as e:
            print(f"Error renaming file or folder: {e}")

    def file_size(self, file_name):
        try:
            size = os.path.getsize(file_name)
            print(f"Size of \"{file_name}\": {size} bytes")
        except FileNotFoundError:
            print("File not found.")
        except OSError as e:
            print(f"Error retrieving file size: {e}")

    def show_help(self):
        help_text = '''
Available Commands:
- mkdir folder_name: Create a folder
- touch file_name: Create an empty file
- ls: List directory contents
- cd directory_name: Change directory
- rm file_name: Remove a file
- tree: Display directory structure
- pwd: Show current working directory
- rename old_name new_name: Rename a file or folder
- size file_name: Show the size of a file
- log: Display recent file system commands
- help: Show this help message
- exit: Exit the program
'''
        print(help_text)

    def log_command(self, command):
        logging.info(command)

    def view_logs(self):
        try:
            with open('fs_emulator.log', 'r') as log_file:
                print("Recent Logs:")
                print(log_file.read())
        except FileNotFoundError:
            print("No logs available.")

    def timestamped_file(self, file_name):
        try:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            new_name = f"{file_name}_{timestamp}"
            self.touch_file(new_name)
            print(f"File created with timestamp: {new_name}")
        except Exception as e:
            print(f"Error creating timestamped file: {e}")

def main():
    fs = FileSystem()
    while True:
        cmd = input('Enter command: ')
        fs.log_command(cmd)
        try:
            if cmd.startswith('mkdir'):
                _, folder_name = cmd.split(maxsplit=1)
                fs.create_folder(folder_name)
            elif cmd.startswith('touch'):
                _, file_name = cmd.split(maxsplit=1)
                fs.touch_file(file_name)
            elif cmd == 'ls':
                fs.list_directory()
            elif cmd.startswith('cd'):
                _, directory_name = cmd.split(maxsplit=1)
                fs.change_directory(directory_name)
            elif cmd.startswith('rm'):
                _, file_name = cmd.split(maxsplit=1)
                fs.remove_file(file_name)
            elif cmd.startswith('rename'):
                _, old_name, new_name = cmd.split(maxsplit=2)
                fs.rename(old_name, new_name)
            elif cmd.startswith('size'):
                _, file_name = cmd.split(maxsplit=1)
                fs.file_size(file_name)
            elif cmd == 'tree':
                fs.display_tree()
            elif cmd == 'pwd':
                fs.print_working_directory()
            elif cmd == 'help':
                fs.show_help()
            elif cmd == 'log':
                fs.view_logs()
            elif cmd.startswith('timestamp'):
                _, file_name = cmd.split(maxsplit=1)
                fs.timestamped_file(file_name)
            elif cmd == 'exit':
                break
            else:
                print("Unknown command. Type 'help' for available commands.")
        except ValueError:
            print("Invalid command format. Check 'help' for correct usage.")

if __name__ == '__main__':
    main()
