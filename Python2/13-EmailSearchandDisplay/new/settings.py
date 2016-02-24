import datetime

RECIPIENTS = (('Frank', 'frank@gmail.com'), ('Michael', 'michael@gmail.com'), ('Annie', 'annie@gmail.com'))
STARTTIME = datetime.datetime(2014, 12, 12)
DAYCOUNT = 10

TABLEDEF = """\
CREATE TABLE messages(
    msgID INTEGER AUTO_INCREMENT PRIMARY KEY,
    msgMessageID VARCHAR(128),
    msgDate DATETIME,
    msgSenderName VARCHAR(128),
    msgSenderAddress VARCHAR(128),
    msgRecipientName VARCHAR(128),
    msgRecipientAddress VARCHAR(128),
    msgText LONGTEXT
)"""
