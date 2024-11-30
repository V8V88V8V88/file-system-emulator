
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

