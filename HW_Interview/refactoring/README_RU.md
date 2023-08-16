Почтовый клиент

Класс EmailClient предоставляет упрощенный интерфейс для отправки и получения электронных писем с использованием протоколов SMTP и IMAP.

Возможности
Отправка писем с вложениями
Получение писем на основе заголовка темы
Надежная обработка ошибок и управление соединениями

Установка
Клонируйте репозиторий:
git clone https://github.com/your_username/email-client.git

Установите необходимые пакеты:
pip install -r requirements.txt

Использование
Импортируйте класс EmailClient:
from email_client import EmailClient

Создайте экземпляр класса EmailClient с данными вашего SMTP и IMAP серверов:
email_client = EmailClient(smtp_server, smtp_port, imap_server, imap_port, username, password)
Отправка письма:
subject = 'Тема'
recipients = ['recipient1@example.com', 'recipient2@example.com']
message = 'Тело письма.'
email_client.send_email(subject, recipients, message)

Получение письма:
received_email = email_client.receive_email(subject)
print("Тема полученного письма:", received_email['Subject'])
