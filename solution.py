import os
import tempfile


class File:
    def __init__(self, path):
        if not os.path.exists(path):
            open(path, "w")
        self.path = path
        self.current = 0

    def read(self):
        with open(self.path, "r") as f:
            return f.read()

    def write(self, new_text):
        with open(self.path, "w") as f:
            f.write(new_text)

    def __add__(self, other):
        content1 = self.read()
        content2 = other.read()
        result_file = File(tempfile.gettempdir() + "/add_result")
        result_file.write(content1 + content2)
        return result_file

    def count_lines(self):
        return sum(1 for line in open(self.path))

    def __str__(self):
        return self.path

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.count_lines():
            self.current = 0
            raise StopIteration
        result = self.read().split("\n")[self.current] + "\n"
        self.current += 1
        return result


if __name__ == "__main__":
    test = File("some_filename")
    test2 = File("some_filename_1")
    test3 = test + test2
