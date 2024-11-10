import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText
 
def send_email_yandex(sender_email, password, receiver_email, subject, body): 
    # Настройка SMTP-сервера 
    smtp_server = "smtp.yandex.ru" 
    smtp_port = 465
 
# Создаем объект сообщения 
    msg = MIMEMultipart() 
    msg['From'] = sender_email 
    msg['To'] = receiver_email 
    msg['Subject'] = subject
 
# Добавляем тело письма 
    msg.attach(MIMEText(body, 'plain'))
 
    try: 
    # Установка соединения с сервером 
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.login(sender_email, password)
 
    # Отправка письма 
        server.send_message(msg) 
        print("Письмо успешно отправлено")
 
    except Exception as e: 
        print(f"Произошла ошибка: {e}")
 
    finally: 
    
    # Закрытие соединения с сервером \
        server.quit()
 
sender_email = "почта отправителя" 
password = "пароль отправителя" 
# Пароль приложения из настроек Яндекса 
receiver_email = "почта получателя" 
subject = "тема сообщения" 
body = "текст сообщения"
 
send_email_yandex(sender_email, password, receiver_email, subject, body)
