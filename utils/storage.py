from utils.Exceptions import storage_error


class Storage:
    def __init__(self, file_path):
        self.file_path = file_path

    def load(self):
        try:
            with open(self.file_path, "r", encoding="utf-8") as file:
                return [
                    line.rstrip("\n").split("|")
                    for line in file
                    if line.strip()
                ]
        except FileNotFoundError:
            return []
        except OSError as error:
            raise storage_error() from error

    def save(self, data):
        try:
            with open(self.file_path, "w", encoding="utf-8") as file:
                for row in data:
                    file.write("|".join(str(value) for value in row) + "\n")
        except OSError as error:
            raise storage_error() from error
