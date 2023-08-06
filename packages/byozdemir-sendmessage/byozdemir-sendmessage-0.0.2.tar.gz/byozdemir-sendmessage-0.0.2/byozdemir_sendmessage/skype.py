from skpy import Skype
class Messager:
    def __init__(self,**data) -> None:
        self.mail = data.get('mail')
        self.password = data.get('password')

    def sendMessage(self,receiver,msg,**data):
        sk = Skype(self.mail,self.password)
        contact = sk.contacts[receiver]
        contact.chat.sendMsg(msg)

    def help(self):
        print("""
Usage
    messager = byozdemir_sendmessage.getProvider("skype",mail='',password='')
    message.sendMessage('liveid','message here')

    --- Contact list ---
    messager = byozdemir_sendmessage.getProvider("skype",mail='',password='')
    contacts = messager.getContacts()
    for contact in contacts:
        print(contact)
        """)

    def getContacts(self):
        sk = Skype(self.mail,self.password)
        contact = sk.contacts
        return contact