import telepot
class Messager:
    def __init__(self,**data) -> None:
        self.token = data.get('key')

    def sendMessage(self,receiver_id,message,**data):
        bot = telepot.Bot(self.token)
        bot.sendMessage(receiver_id,message)

    def help(self):
        print("""
Usage
    messager = byozdemir_sendmessage.getProvider("telegram",key='telegramkey')
    message.sendMessage('telegramid','message here')
        """)
