""" The smtplib module helps us send emails while the rest of two classes
imported from email.mime.multipart module help us in send an email
capable of containing multipart like text, HTML and attachments. """
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_email(my_message):
    """ This is the function that will send the email to the reciever."""
    message = MIMEMultipart()
    message["from"] = "clever khan"
    message["to"] = "Reciever Email"
    message["subject"] = "Tech News by Khan"
    message.attach(MIMEText(my_message))

    with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.login("Sender Email", "Sender Password") # NOQA
        smtp.send_message(message)
        print("Email has successfully been sent")
send_email("Pthon Is Awesome | here you will write the body of your email")
