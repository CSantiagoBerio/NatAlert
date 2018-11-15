class Event:

    def _init_(self):
        self.type = ""
        self.location = ""
        self.sendto = []
        self.comment = ""

    def create(self, type, location, sendto, comment):
        self.type = type
        self.location = location
        self.sendto = sendto
        self.comment = comment

    def settype(self, type):
        self.type = type

    def gettype(self):
        return self.type

    def setlocation(self, location):
        self.location = location

    def getlocation(self):
        return self.location

    def setsendto(self, sendto):
        self.sendto = sendto

    def getsendto(self):
        return self.sendto
