import smtplib
from email.mime.text import MIMEText
from config import SMTP_EMAIL, SMTP_PASSWORD

def send_alert(tweet_text, sentiment_score):
    subject = "Bitcoin Alert"
    body = f"Influencer Tweet: {tweet_text}\nSentiment Score: {sentiment_score}"
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = SMTP_EMAIL
    msg['To'] = SMTP_EMAIL

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SMTP_EMAIL, SMTP_PASSWORD)
        server.sendmail(SMTP_EMAIL, SMTP_EMAIL, msg.as_string())
        server.quit()
        print("Alert sent!")
    except Exception as e:
        print("Failed to send alert:", e)
