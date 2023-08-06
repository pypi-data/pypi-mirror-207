import telepot
class Messager:
    def __init__(self,**data) -> None:
        self.token = data.get('key')

    def sendMessage(self,receiver_id,message,**data):
        bot = telepot.Bot(self.token)
        bot.sendMessage(receiver_id,message)
