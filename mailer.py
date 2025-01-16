import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "goyaldanish542@gmail.com"
password = "kwfy lhga medv gpqs"

server = "smtp.gmail.com"
smtp_port = 587


def SendMail(email, emailBodyMessage, warning=False):
    subject = 'Maximum Absentee has been limit to be reached' if not warning else 'Warning for reaching maximum attendance limit'


    body = emailBodyMessage
    dest = email

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = dest
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))


    try:
        with smtplib.SMTP(server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, dest, text)
            print("email sent successfully")
    except Exception as e:
        print(f"Error : {e}")
    pass