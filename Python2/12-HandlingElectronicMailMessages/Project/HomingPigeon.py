#!usr/bin/env python3
#            A function returns a MIMME (Multipurpose Internet Mail Extensions)
#                       HomingPigeon.py
# By: Fadel Berakdar
# Date: 30 July 2015

"""
Write a function that takes an email address, a string, and a list argument.
It should return an email message addressed
to the email address passed as the first argument, with the second argument as
the message body. If the list is
non-empty, then each list item should be treated as the name of a file and the
corresponding file should be attached
(with an appropriate MIME type) to the message.

Please include any files to attach in the same folder as your program.
There is no need to send it as an email with
smtp, though you may wish to print it as a string as a part of testing.

"""

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.audio import MIMEAudio
import mimetypes
import os

os.getcwd()

path = "/Users/AboAlfdel/Dropbox/Python/Code/Python2/12-HandlingElectronic" \
       "MailMessages/s/"
# path = "v:\\workspace\\HandlingElectronicEmailMessages_Homework\\src\\"


def messenger(address, body, attachments):
    # Shadows name "attachments" from outer scope!!!
    msg = MIMEMultipart()
    msg['To'] = address
    text_msg = MIMEText(body, 'plain')
    msg.attach(text_msg)

    if attachments:
        for fn in attachments:
            _type, subtype = mimetypes.guess_type(fn)[0].split('/')

            if _type == "text":
                fp = open(fn, "r")
                mime = MIMEText(fp.read(), _subtype=subtype)
            elif _type == "image":
                fp = open(fn, 'rb')
                mime = MIMEImage(fp.read(), _subtype=subtype)
            elif _type = "audio":
                fp = open(fn, 'rb')
                mime = MIMEAudio(fp.read(), _subtype=subtype)
            else:
                fp = open(fn, 'rb')
                # MIMEBase is the parent of a family of classes that provide
                # functionality for specific MIME types.
                mime = MIMEBase(type, subtype)
                mime.set_payload(fp.read())
                mime.add_header('Content-Disposition', 'attachment',
                                filename=os.path.basename(fn))
            msg.attach(mime)
            fp.close()
    return msg


if __name__ == "__main__":
    attach1 = os.path.join(path, "python_logo.png")
    attach2 = os.path.join("declaration.txt")
    attachments = [attach1, attach2]
    print(messenger("mfb.bioinfo@gmail.com", "Declaration of independence",
                    attachments))
