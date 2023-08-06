import smtplib
from email.mime.text import MIMEText
class Messager:
    def __init__(self,**data) -> None:
        self.SMTP_user = data.get('user')
        self.SMTP_password = data.get('password')
        self.SMTP_server = data.get('server')
        self.SMTP_port =  data.get('port')

    def sendMessage(self,receiver_id,message,**data):
        msg = MIMEText(message)
        msg['Subject'] = data.get('subject')
        msg['From'] = self.SMTP_user
        msg['To'] = receiver_id
        smtp_server = smtplib.SMTP_SSL(self.SMTP_server, self.SMTP_port)
        smtp_server.login(self.SMTP_user, self.SMTP_password)
        smtp_server.sendmail(self.SMTP_user, receiver_id, msg.as_string())
        smtp_server.quit()

    def help(self):
        print("""
Usage
    messager = byozdemir_sendmessage.getProvider("mail",user='user',password='password',server='server',port='port')
    message.sendMessage('targetMail','message here',subject='subject')
        """)