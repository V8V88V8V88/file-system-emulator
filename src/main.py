
import os

class FileSystem:
    def __init__(self):
        self.current_directory = os.getcwd()

    def create_folder(self, folder_name):
    def create_file(self, file_name):
        with open(file_name, "w") as f:
            f.write("")
        os.makedirs(folder_name, exist_ok=True)


def main():
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

