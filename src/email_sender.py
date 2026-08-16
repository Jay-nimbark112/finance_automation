import os
import smtplib

from pathlib import Path
from dotenv import load_dotenv

from email.message import EmailMessage


load_dotenv()


def create_email():

    sender = os.getenv("EMAIL_ADDRESS")
    receiver = os.getenv("RECEIVER_EMAIL")

    message = EmailMessage()

    message["From"] = sender
    message["To"] = receiver
    message["Subject"] = "Automated Sales Report"

    message.set_content(
        """Hello,

Please find attached the latest sales reports.

Attachments:
- Sales Excel Report
- Sales PDF Report

Regards,
Automation System
"""
    )

    return message


def attach_file(message, file_path):

    file_path = Path(file_path)

    with open(file_path, "rb") as file:

        file_data = file.read()

    message.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_path.name
    )


def send_email(message):

    sender = os.getenv("EMAIL_ADDRESS")
    password = os.getenv("EMAIL_PASSWORD")

    with smtplib.SMTP(
        "smtp.gmail.com",
        587
    ) as server:

        server.starttls()

        server.login(
            sender,
            password
        )

        server.send_message(message)

    print("Email sent successfully!")