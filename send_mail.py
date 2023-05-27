import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def attatch_file(filename,message):
    # filename = "interview_scores.csv"
    filepath = "./" + filename

    with open(filepath, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload((attachment).read())

    encoders.encode_base64(part)
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    return message.attach(part)

sender_email = "hack.acs.drr@gmail.com"
receiver_email = "revathikrish001@gmail.com"
password = "acs@1234"
app_password='locignbulcnmrezu'

message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "candidates interview scores"

body = "Please find the scores file of interviews taken today"
message.attach(MIMEText(body, "plain"))

attatch_file("Interview_scores.csv",message=message)
attatch_file("Interview_details.csv",message=message)
# filename = "interview_scores.csv"
# filepath = "./" + filename

# with open(filepath, "rb") as attachment:
#     part = MIMEBase("application", "octet-stream")
#     part.set_payload((attachment).read())

# encoders.encode_base64(part)
# part.add_header(
#     "Content-Disposition",
#     f"attachment; filename= {filename}",
# )

# message.attach(part)
text = message.as_string()

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, text)
