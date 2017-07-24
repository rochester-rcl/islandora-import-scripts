import os


class FileInfo:
    """Holds basic file information """

    def __init__(self, name, extension, path):
        self.name = name
        self.extension = extension
        self.path = path

    def get_file_name(self):
        return self.name + self.extension

    def get_full_path(self):
        return os.path.join(self.path, (self.name + self.extension))

    def to_string(self):
        return ("name = " + self.name + " extension = " + self.extension + " path = " +
                self.path)

    def to_csv(self):
        return self.name + ", " + self.get_full_path()

