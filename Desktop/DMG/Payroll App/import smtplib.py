import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def send_form_as_email(receiver_email, form_path):
    sender_email = "jesusrojasct@gmail.com"
    sender_password = "asupolala19"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Daily Sales Form"

    # Body of the email (optional)
    body = "Please find attached the daily sales form."
    message.attach(MIMEText(body, "plain"))

    # Open the form file to be attached
    with open(form_path, "rb") as attachment:
        # Add file as application/octet-stream
        attached_form = MIMEBase("application", "octet-stream")
        attached_form.set_payload(attachment.read())

    # Encode the form in base64
    encoders.encode_base64(attached_form)

    # Add header as key/value pair to the attached form
    attached_form.add_header(
        "Content-Disposition",
        f"attachment; filename= {form_path}",
    )

    # Attach the form to the email message
    message.attach(attached_form)

    try:
        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.example.com", 587)  # Update with your SMTP server details
        server.starttls()
        server.login(sender_email, sender_password)
        # Send email
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")
    finally:
        # Quit the SMTP server
        server.quit()

# Usage example:
receiver_email = "jesusrojasct@gmail.com"
form_file_path = "path/to/daily_sales_form.pdf"  # Update with your form file path
send_form_as_email(receiver_email, form_file_path)
