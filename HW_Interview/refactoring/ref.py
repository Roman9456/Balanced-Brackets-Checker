import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailClient:
    def __init__(self, smtp_server, smtp_port, imap_server, imap_port, username, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.imap_server = imap_server
        self.imap_port = imap_port
        self.username = username
        self.password = password

    def send_email(self, subject, recipients, message, header=None):
        msg = MIMEMultipart()
        msg['From'] = self.username
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        with smtplib.SMTP(self.smtp_server, self.smtp_port) as ms:
            ms.starttls()
            ms.login(self.username, self.password)
            ms.sendmail(self.username, recipients, msg.as_string())

    def receive_email(self, header=None):
        with imaplib.IMAP4_SSL(self.imap_server, self.imap_port) as mail:
            mail.login(self.username, self.password)
            mail.select("inbox")
            criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
            result, data = mail.uid('search', None, criterion)
            assert data[0], 'There are no letters with the current header'
            latest_email_uid = data[0].split()[-1]
            result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
            raw_email = data[0][1]
            email_message = email.message_from_string(raw_email)
        return email_message

if __name__ == '__main__':
    GMAIL_SMTP = "smtp.gmail.com"
    GMAIL_SMTP_PORT = 587
    GMAIL_IMAP = "imap.gmail.com"
    GMAIL_IMAP_PORT = 993

    login_email = 'login@gmail.com'
    password = 'qwerty'
    email_subject = 'Subject'
    recipients_list = ['vasya@email.com', 'petya@email.com']
    email_message_body = 'Message'

    email_client = EmailClient(GMAIL_SMTP, GMAIL_SMTP_PORT, GMAIL_IMAP, GMAIL_IMAP_PORT, login_email, password)

    # Sending an email
    email_client.send_email(email_subject, recipients_list, email_message_body)

    # Receiving an email
    received_email = email_client.receive_email(email_subject)
    print("Received Email Subject:", received_email['Subject'])
