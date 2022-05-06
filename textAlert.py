import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def sendMail(data, email, pas, sms_gate):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(email, pas)
        msg = MIMEMultipart()
        msg['From'] = email
        msg['To'] = ", ".join(sms_gate)
        msg['Subject'] = 'GPU STOCK ALERT'
        body = data
        msg.attach(MIMEText(body, 'plain'))

        sms = msg.as_string()
        server.sendmail(email, sms_gate, sms)
        server.quit()


    except smtplib.SMTPResponseException as e:
        error_code = e.smtp_code
        error_message = e.smtp_error
        print(error_code)
        print(error_message)

    return