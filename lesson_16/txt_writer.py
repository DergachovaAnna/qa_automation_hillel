class TxtWriter:

    def __init__(self, file_path):
        self.file_path = file_path

    def write(self, new_data, mode):
        with open(self.file_path, mode) as file:
            text = file.write(new_data)
        return text
