# send_mail.py
# Python 3.5

"""
Utility library to send mail
Sender - vin.raspi@gmail.com; Receiver - vinovator@gmai.com
Given a subject and mail content, send a mail
"""

import smtplib
from IGNORE import raspi_secrets  # Untracked py to carry secrets

SMTP_server = "smtp.gmail.com"  # google smtp server


# List of constants inherited from an untracked file
mail_id = raspi_secrets.login["mail"]
pwd = raspi_secrets.login["password"]

receiver = {
    "name": "Vinoth",
    "email": "vinovator@gmail.com"
}


def send_mail(recieved_subject, received_body):
    """ Given the mail subject and content send mail """

    # Login to smtp server
    smtpObj = smtplib.SMTP(SMTP_server, 587)  # 587 indicates TLS encryption
    # Send a hello message to establish connection, returns 250 if success
    smtpObj.ehlo()
    smtpObj.starttls()  # start TLS encryption

    # login to server, 235 is returned if success
    smtpObj.login(mail_id, pwd)

    # Send mail
    to_name = receiver["name"]
    to_email = receiver["email"]

    mail_subject = recieved_subject
    mail_body = "Hello {0},\n\n {1}. \n\n Cheers".format(to_name,
                                                         received_body)

    smtpObj.sendmail(mail_id,
                     to_email,
                     "subject:" + mail_subject + "\n" + mail_body)

    # Finally disconnect from SMTP server
    smtpObj.quit()
