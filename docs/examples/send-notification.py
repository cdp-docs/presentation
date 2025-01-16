import smtplib
from email.mime.text import MIMEText

def send_payment_request(subscriber_email, amount, payment_link):
    subject = "Payment Request for Subscription"
    body = f"Dear Subscriber,\n\nPlease approve your payment of {amount} to continue your subscription.\n\nClick here to approve: {payment_link}"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'service@provider.com'
    msg['To'] = subscriber_email

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login('anna.baker.313@gmail.com', 'Greyson$86')
        server.sendmail('anna.baker.313@gmail.com', subscriber_email, msg.as_string())

send_payment_request("amarie.engle@gmail.com", "0.1 ETH", "http://yourwebsite.com/approve-payment")

