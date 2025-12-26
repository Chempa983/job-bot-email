import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = os.environ["SMTP_HOST"]
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ["SMTP_USER"]
SMTP_PASS = os.environ["SMTP_PASS"]
EMAIL_TO  = os.environ["EMAIL_TO"]

def send(subject, body):
    msg = MIMEMultipart()
    msg["From"] = SMTP_USER
    msg["To"] = EMAIL_TO
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain", "utf-8"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as s:
        s.starttls()
        s.login(SMTP_USER, SMTP_PASS)
        s.sendmail(SMTP_USER, [EMAIL_TO], msg.as_string())

def main():
    body = (
        "✅ Job Bot – TEST\n\n"
        "Ako vidiš ovaj mejl, GitHub + Gmail konekcija radi.\n"
        "Sledeće: pravi izvori poslova + 88% match filter.\n"
    )
    send("Job Bot – test email", body)

if __name__ == "__main__":
    main()
