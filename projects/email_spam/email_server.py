import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email content
sender_email = "your_email@example.com"
subject = "Subject of the Email"



def send_spam():
    # get the html content to say
    with open("cool.html", "r") as file:
        html_content = file.read()

    # log into the email server
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("felixshubs@gmail.com", "E11111111")


    message = MIMEMultipart()
    message["Subject"] = subject
    message["From"] = sender_email
    message.attach(MIMEText(html_content, "html"))
    

    
    
    
    
    
    email_addresses = [
    "vthujf6o@gmail.com",
    "kgyakq2l@gmail.com",
    "rwmwlb5r@gmail.com",
    "qmtayg4z@gmail.com",
    "ubhzpb8c@gmail.com",
    "xgtwic1n@gmail.com",
    "mmhbkc9e@gmail.com",
    "slzqvd5r@gmail.com",
    "yvwzns3g@gmail.com",
    "vcphtq4s@gmail.com"
    ]
    for receiver_email in email_addresses:
        
        message["To"] = receiver_email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("done")

        

    server.quit()

send_spam()