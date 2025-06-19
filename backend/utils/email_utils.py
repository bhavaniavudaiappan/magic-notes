# backend/utils/email_utils.py

import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv

load_dotenv()

def send_magic_link(to_email: str, token: str):
    msg = EmailMessage()
    msg['Subject'] = '🪄 Your Magic Notes Login Link'
    msg['From'] = os.getenv("EMAIL_USER")
    msg['To'] = to_email

    magic_url = f"{os.getenv('BASE_URL')}/?token={token}"

    # ✨ Custom email content
    msg.set_content(f"""
    Hello Magical Note Taker! ✨

    You requested a login link to Magic Notes.

    Click the link below to access your magical notebook:
    {magic_url}

    If you didn’t request this, simply ignore this email. 🧙‍♂️

    Stay enchanted,
    The Magic Notes Team
    """)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(os.getenv("EMAIL_USER"), os.getenv("EMAIL_PASS"))
        smtp.send_message(msg)
