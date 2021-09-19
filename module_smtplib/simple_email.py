import os
import smtplib

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

with smtplib.SMTP("smtp-mail.outlook.com", 587) as smtp:
    # identify with the mail server
    smtp.ehlo()
    # encrypt traffic
    smtp.starttls()
    # need to identify ourselfs again after encryption
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = "This is the subject"
    body = "This is the body part"

    # header required & couples new lines to separate the header and the body part
    msg = f"Subject: {subject}\n\n{body}"

    # arguments: sender, receiver, message
    # here i am emailing to myself
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
