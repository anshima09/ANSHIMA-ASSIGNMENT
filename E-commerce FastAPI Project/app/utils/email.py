import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from fastapi import HTTPException, status
from dotenv import load_dotenv
import os
load_dotenv()
def sending_email_with_token(
   # sender: str,
   # password: str,
    receiver: str,
    reset_token: str,
    receiver_name: str
):
    sender = os.getenv("EMAIL_SENDER")
    password = os.getenv("EMAIL_PASSWORD")
    subject_line = "Password Reset Token for E-commerce login"
    
    body = f"""
Hello {receiver_name},

We received a request to reset your password for your E-commerce account.

Your password reset token is:

    {reset_token}

This token is valid for only 5 minutes. If you did not request a password reset, you can safely ignore this email.

Thank you for using our service!

Best regards,  
E-commerce Support Team
"""

    msg = MIMEMultipart()
    msg['From'] = sender
    msg['To'] = receiver
    msg['Subject'] = subject_line
    msg.attach(MIMEText(body, "plain"))

    try:
        # Note: smtplib is blocking; for true async use an async mail library.
        with smtplib.SMTP("smtp.gmail.com", 587) as my_server:
            my_server.starttls()
            my_server.login(sender, password)
            my_server.sendmail(sender, receiver, msg.as_string())
            print("email sent successfully")
    except Exception as e:
        print("Error in sending mail : ", e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to send reset email. Please try again later."
        )