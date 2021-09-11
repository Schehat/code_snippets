import os
import smtplib

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

# using debugging server in localhost to not send myself everytime an email.
# Use this command in terminal: python -m smtpd -c DebuggingServer -n localhost:1025
# and then run script
with smtplib.SMTP("localhost", 1025) as smtp:
    subject = "This is the subject"
    body = "This is the body part"
    msg = f"Subject: {subject}\n\n{body}"
    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)
