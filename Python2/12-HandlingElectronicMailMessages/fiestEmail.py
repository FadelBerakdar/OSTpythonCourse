#  **** Sending My First Email Using Python Script ****

import smtplib
import email
import datetime

msg = email.message_from_file(open("example-email.txt"))
msg["Orig-date"] = datetime.datetime.now().strftime("%d %b %Y %H:%M:%S -0600")
msg['X-Holden-Web'] = "Root beer for everyone!"


srv = smtplib.SMTP("smtp.gmail.com", 587)
srv.ehlo()
srv.starttls()
srv.login("fadijado@gmail.com", "23688mfb999705949")
srv.sendmail(msg["From"], msg["To"],msg.as_string())
srv.quit()

