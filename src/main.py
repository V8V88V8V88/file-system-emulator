import os
import logging

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
- help: Show this help message
- exit: Exit the program
'''
        print(help_text)

    def log_command(self, command):
        logging.info(command)

def main():
    fs = FileSystem()
    while True:
        cmd = input('Enter command: ')
        fs.log_command(cmd)
        if cmd.startswith('mkdir'):
            _, folder_name = cmd.split()
            fs.create_folder(folder_name)
        elif cmd.startswith('touch'):
            _, file_name = cmd.split()
            fs.touch_file(file_name)
        elif cmd.startswith('ls'):
            fs.list_directory()
        elif cmd.startswith('cd'):
            _, directory_name = cmd.split()
            fs.change_directory(directory_name)
        elif cmd.startswith('rm'):
            _, file_name = cmd.split()
            fs.remove_file(file_name)
        elif cmd == 'tree':
            fs.display_tree()
        elif cmd == 'pwd':
            fs.print_working_directory()
        elif cmd == 'help':
            fs.show_help()
        elif cmd == 'exit':
            break
        else:
            print("Unknown command. Type 'help' for available commands.")

if __name__ == '__main__':
    main()
