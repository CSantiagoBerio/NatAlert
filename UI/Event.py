class Event:
    def __init__(self):
        self.type = ""
        self.location = ""
        self.sendto = []
        self.comment = ""

    def create(self, type, location, sendto, comment):
        self.type = type
        self.location = location
        self.sendto = sendto
        self.comment = comment
        return {'Event': self.type, 'Location': self.location, 'SendTo': self.sendto, 'Data': self.comment}

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
