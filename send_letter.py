import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#from email.mime.base import MIMEImage

smpt_server = 'smtp.mail.ru'
smpt_port = 465 #меняется
smpt_user = 'почта отправителя'
smpt_pass = 'пароль отправителя'

message = MIMEMultipart()
message['From'] = 'почта отправителя'
message['To'] = 'Почта получателя'
message['Subgect'] = 'Тема сообщения'

message.attach(MIMEText('Текст сообщения', 'plain'))

with smtplib.SMTP(smpt_server, smpt_port) as smtp:
  
  server.starttls()
  server.login(почта отправителя, пароль отправителя)
  server.message('Текст сообщения')
  server.quit()
