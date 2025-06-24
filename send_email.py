import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from email.mime.text import MIMEText
import os

def send_email():
    url = 'https://github.com/Deepandeeps29/All_Report.git'
    sender = 'deepanvinayagam1411@gmail.com'
    recipient = [
        'deepanvinayagam1411@gmail.com',
        'deepanvinayagam2912@gmail.com',
        'deepanvinayagam6382@gmail.com',
    ]
    subject = 'Pytest Selenium Report'
    app_password = 'bhxu nskk kmyx usyf'

    print("Starting email send...")

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = ', '.join(recipient)
    msg['Subject'] = subject
    # Message Send
    msg.attach(MIMEText("Test execution completed. Report attached.\nQspider_Demo_Module_All_Report", 'plain'))

    try:
        with open("report.html", "rb") as file:
            part = MIMEApplication(file.read(), _subtype="html")
            part.add_header('Content-Disposition', 'attachment', filename="report.html")
            msg.attach(part)
        print("Attached report.html")
    except Exception as e:
        print(f"Failed to attach report.html: {e}")
        return

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, app_password)
            server.send_message(msg)
            print("Email sent successfully!")
            print(f"{url}")
    except Exception as e:
        print(f"Email send failed: {e}")
        print(f"{url}")

if __name__ == "__main__":
    print(f"Current dir: {os.getcwd()}")
    print(f"Contents: {os.listdir()}")
    send_email()
