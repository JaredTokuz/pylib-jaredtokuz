import os


class FileNotFoundError(Exception):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Error: %s" % self.value


def searchForFileDownPath(fileName: str, startingPath=".") -> str:
    for root, dirs, files in os.walk(startingPath):
        for Files in files:
            found = Files.find(fileName)
            if found != -1:
                return root + "/" + fileName
    raise FileNotFoundError("File not found")
