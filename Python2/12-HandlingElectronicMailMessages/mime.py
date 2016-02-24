#         *****  Sending email with multiple content *****


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
import email

#  A MIMEMultipart object automatically sets a couple of headers for you
msg = MIMEMultipart()
msg["From"] = "mfb.biotech@gmail.com"
msg["To"] = "mfb.bioinfo@gmail.com"


text_msg = MIMEText('hello!', 'plain')
html_msg = MIMEText('<strong>hello!</strong>', 'html')
with open("s/python_logo.png","rb") as fb:
    image_msg = MIMEImage(fb.read())


msg.attach(text_msg)
msg.attach(html_msg)

# walk() method which allows you to move through all of the messages parts
# and subparts.
'''

srv = smtplib.SMTP("smtp.gmail.com", 587)
srv.ehlo()
srv.starttls()
srv.login("fadijado@gmail.com", "23688mfb999705949")
srv.sendmail(msg["From"], msg["To"],msg.as_string())
srv.quit()

'''
print(msg.as_string())
print("*" * 30, "\n")
print(text_msg.as_string())
print("*" * 30, "\n")
print(html_msg.as_string())

print("*" * 30, "\n")
print(msg.get_content_type())
print(text_msg.get_content_type())
print(html_msg.get_content_type())
