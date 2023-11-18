from faker import Faker

class Message:
    def __init__(self):
        recievedMessage = ""
        sendMessage = ""

    def setRecievedMessage(self, recievedMessage):
        self.recievedMessage = recievedMessage

    def setSendMessage(self, sendMessage):
        header = "-----------↓  Response From Server------------------\n"
        self.sendMessage = header + sendMessage

    def getSendMessage(self):
        return self.sendMessage

    def choiceMessage(self):
        fake = Faker()
        if "name" in self.recievedMessage.lower(): self.setSendMessage(fake.name())
        elif "address" in self.recievedMessage.lower(): self.setSendMessage(fake.address())
        else: self.setSendMessage(fake.text())