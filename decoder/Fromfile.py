import os.path
from os import path
class Fromfile:
    def __init__(self, filePath, formater):
        #Checks if the file actually exists
        if(path.exists(filePath)):
            self.file2read = open(filePath)
        else:
            raise Exception("The file couldn't be found or doesn't exists!")



test = Fromfile("../README.md", 2)
