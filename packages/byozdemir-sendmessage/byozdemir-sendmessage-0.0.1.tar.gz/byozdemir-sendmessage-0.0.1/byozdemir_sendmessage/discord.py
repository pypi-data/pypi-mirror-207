import requests
class Messager:
    def __init__(self,**data) -> None:
        self.key = data.get('key')

    def sendMessage(self,receiver,msg,**data):
        payload = {
            "content":msg
        }
        header = {
            'authorization':self.key
        }

        r = requests.post(f"https://discord.com/api/v9/channels/{receiver}/messages",data=payload,headers=header)

