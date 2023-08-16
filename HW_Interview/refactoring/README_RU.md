�������� ������
����� EmailClient ������������� ���������� ��������� ��� �������� � ��������� ����������� ����� � �������������� ���������� SMTP � IMAP.

�����������
�������� ����� � ����������
��������� ����� �� ������ ��������� ����
�������� ��������� ������ � ���������� ������������
���������
���������� �����������:


git clone https://github.com/your_username/email-client.git
���������� ����������� ������:


pip install -r requirements.txt
�������������
������������ ����� EmailClient:


from email_client import EmailClient
�������� ��������� ������ EmailClient � ������� ������ SMTP � IMAP ��������:


email_client = EmailClient(smtp_server, smtp_port, imap_server, imap_port, username, password)
�������� ������:


subject = '����'
recipients = ['recipient1@example.com', 'recipient2@example.com']
message = '���� ������.'

email_client.send_email(subject, recipients, message)
��������� ������:


received_email = email_client.receive_email(subject)
print("���� ����������� ������:", received_email['Subject'])