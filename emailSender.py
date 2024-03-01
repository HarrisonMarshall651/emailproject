from email.message import EmailMessage
import ssl
import smtplib
from password import Password

# defining email qualities as objects
email_sender = "harrisonjmarshall@gmail.com"
pass1 = Password("name")
email_receiver = "darksh0gunyt@gmail.com"
subject = 'test2'
body = "This is just another test"

email_receivers = ["darksh0gunyt@gmail.com" , "harrisonblizzard1954@gmail.com"]

# connecting the objects to an actual email format
em = EmailMessage()
em['From'] = email_sender
em["To"] = email_receivers
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

# sending the email

for num in email_receivers:
    print(num)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, pass1.getPass())
        smtp.sendmail(email_sender, email_receivers, em.as_string())

# with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
#    smtp.login(email_sender, email_password)
#    smtp.sendmail(email_sender, email_receiver, em.as_string())
