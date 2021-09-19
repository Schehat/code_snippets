import imghdr  # to classify format of pic. Doing this manually tedious with multiple files
import os
import smtplib
from email.message import EmailMessage

os.chdir(os.path.dirname(__file__))

EMAIL_ADDRESS = os.environ.get("EMAIL_USER")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASS")

# cleaner this way
msg = EmailMessage()
msg["Subject"] = "This is the subject"
msg["From"] = EMAIL_ADDRESS
msg["To"] = EMAIL_ADDRESS  # passing list to address people
msg.set_content("This is the body part")

files = ["pic_1.jpg", "pic_2.png"]

# for file in files:
#     with open(file, "rb") as f:
#         file_data = f.read()
#         file_type = imghdr.what(f.name)
#         file_name = f.name

#     # add picture to mail
#     msg.add_attachment(
#         file_data, maintype="image", subtype=file_type, filename=file_name
#     )

# with pdf's maintype="application", subtype="octet-stream"

# using html in mail. This way either the msg.set_content will be send or this alternative.
# it is possible to block html in mails. That's why alternative will be send first but if it is
# blocked then the plain text will be sended
# Note: using attachment and alternatives at the same time is not possible
msg.add_alternative(
    """
<!DOCTYPE html>
<html>
    <body>
        <h1 style="color:SlateGray;">This is an HTML Email!</h1>
    </body>
</html>
""",
    subtype="html",
)

with smtplib.SMTP("smtp-mail.outlook.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    # instead of sendmail only want to send and do not need to specify sender & receiver
    smtp.send_message(msg)
