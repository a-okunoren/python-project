# Reference for this exercise and even more email exercises: https://realpython.com/python-send-email/

import smtplib
import ssl
# these two are for sending more complex emails
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Some variables needed globally
server = smtplib.SMTP(host='smtp.gmail.com', port=587)

username = 'atoprintsuk@gmail.com'
password = input("Type your email password")

sender = 'Dee Temilope <atoprintsuk@gmail.com>'
receiver = 'deeokunoren@gmail.com'

recipients = ['deeokunoren@gmail.com']

message = """\
Subject: Hi there

This message is sent from Python."""

# Create the plain-text and HTML version of your message
plain_text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html_text = """\
<html>
  <body>
    <p>Hi,<br>
       How are you?<br>
       <a href="http://www.realpython.com">Real Python</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""


def configure_mail(email_type):  # Configure imbox then send email based on email_type
    # assert(isinstance(receiver_email, list))  # throw error if receiver_email isnt a list
    # create a secure SSL context
    context = ssl.create_default_context()
    try:
        # declare a server instance
        #server = smtplib.SMPT_SSL(host='smtp.gmail.com', port=587)
        server.ehlo()  # config
        server.starttls(context=context)  # enable TLS - more config
        server.ehlo()

     # login to email
        server.login(username, password)

     # send email by calling any of the below functions
        if email_type == 1:
            send_mail_simple(message, sender, receiver)
        elif email_type == 2:
            send_mail_html(plain_text, html_text,
                           "Multipart Email Test!", sender, receiver)
    except Exception as e:  # if there are any errors they are stored in e
        print(e)
    finally:  # the finally clause will execute as the last task before the try statement completes
        server.quit()  # terminate connection to the server
        print("Email Sent!")


def send_mail_simple(text, sender_email, receiver_email):  # send simple email message

    server.sendmail(sender_email, receiver_email, text)


def send_mail_html(text, html, subject, sender_email, receiver_email):  # initialise string params
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Convert plain and html into MIMETEXT objects (i guess those are email formats)
    text_part = MIMEText(text, "plain")
    html_part = MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first
    msg.attach(text_part)
    msg.attach(html_part)

    # send email from sender_email to receiver_email - need to comvert that multipart thingy to string sha
    server.sendmail(sender_email, receiver_email, msg.as_string())


configure_mail(2)
