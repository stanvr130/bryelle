from django.core.mail import EmailMessage

def send_email(data):
    to = data.get(to)
    subject = data.get(subject)
    