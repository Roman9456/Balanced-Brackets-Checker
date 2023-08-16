
Email Client
The EmailClient class provides a simplified interface for sending and receiving emails using SMTP and IMAP protocols.

Features
Sending emails with attachments
Receiving emails based on header subject
Robust error handling and connection management
Installation
Clone the repository:



git clone https://github.com/your_username/email-client.git
Install the required packages:


pip install -r requirements.txt
Usage
Import the EmailClient class:

from email_client import EmailClient
Create an instance of the EmailClient class with your SMTP and IMAP server details:


email_client = EmailClient(smtp_server, smtp_port, imap_server, imap_port, username, password)
Sending an email:


subject = 'Subject'
recipients = ['recipient1@example.com', 'recipient2@example.com']
message = 'This is the email message body.'

email_client.send_email(subject, recipients, message)
Receiving an email:


received_email = email_client.receive_email(subject)
print("Received Email Subject:", received_email['Subject'])