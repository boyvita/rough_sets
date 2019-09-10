class ReaderPlus:
    def __init__(self, fileName):
        self.fileName = fileName
        self.currentFile = open(fileName, "r+")
        self.modeRead = True
        self.numLine = 1

    def readLine(self):
        line = ""
        print(str(self.numLine), end=". ")
        if self.modeRead:
            line = self.currentFile.readline()
            if not line:
                self.modeRead = False
                self.currentFile.close()
                self.currentFile = open("test.txt", "a")
            else:
                print(line)
        if not self.modeRead:
            line = input()
            self.currentFile.write(line + "\n")
        self.numLine += 1
        return line
