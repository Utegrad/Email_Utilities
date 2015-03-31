#!/usr/bin/env python

"""
Module Docstring
"""
""" Created by matthew on '3/30/15' """

import sys
import smtplib
from email.mime.text import MIMEText


class EmailClient():
    def __init__(self, msg_file=None,rcpt_addr=None, msg_sender=None,
                 msg_subject=None, username=None, password=None, snd_host='localhost',
                 port=587, tls=False):
        self.rcpt_addr = rcpt_addr
        self.msg_sender= msg_sender
        self.msg_subject = msg_subject
        self.msg_file = msg_file
        self.tls = tls
        self.msg = self.create_msg()
        self.msg['Subject'] = self.msg_subject
        self.msg['From'] = self.msg_sender
        self.msg['To'] = self.rcpt_addr
        self.smtp_client = smtplib.SMTP(snd_host, port)
        self.smtp_username = username
        self.smtp_password = password


    def create_msg(self, other_file=None):
        if other_file is None:
            filename = self.msg_file
        else:
            filename = other_file
        f = open(filename, 'rb')
        msg = MIMEText(f.read())
        f.close()
        return msg

    def send_msg(self):
        tls = self.tls
        if tls is True:
            self.smtp_client.starttls()
            self.smtp_client.login(self.smtp_username, self.smtp_password)
        result = self.smtp_client.sendmail(self.msg_sender, self.rcpt_addr, self.msg.as_string(),)
        self.smtp_client.quit()
        return result

#

def main(args):
    """ main Docstring """
    mail_client = EmailClient('another file.txt', 'recipient@somewhere.com',
                              'sender@someplace.com', 'Test message with Python',
                              'username', 'password', 'smtp.server.com',
                              587, True)
    mail_client.create_msg()
    status = mail_client.send_msg()
    print status

    pass


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))


