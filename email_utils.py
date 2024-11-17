from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pathlib import Path
# Email Configuration
conf = ConnectionConfig(
    MAIL_USERNAME="tpeddireddy007@gmail.com",
    MAIL_PASSWORD="ratqurhtxryhkvtb",
    MAIL_FROM="tpeddireddy007@gmail.com",
    MAIL_PORT=587,
    MAIL_SERVER="smtp.gmail.com",
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True
)


async def send_invitation_email():
    recipients = [
	"shraddha@aviato.consulting",
        "pooja@aviato.consulting",
        "prijesh@aviato.consulting",
        "hiring@aviato.consulting",
	"tpeddireddy007@gmail.com"  # Add more recipients as needed
    ]

    # Load the HTML template
    html_template_path = Path("email_template.html")  # Ensure this file exists in the project directory
    html_content = html_template_path.read_text()

    # Replace placeholders in the HTML template (if needed)
    # Example: Replace the button link or any dynamic content
    html_content = html_content.replace(
        "http://54.80.159.115:8000/docs", "http://54.80.159.115:8000/docs"
    )

    # Create the email message
    message = MessageSchema(
        subject="API Documentation Invitation",
        recipients=recipients,  # List of recipients
        body=html_content,  # Use the HTML template as the email body
        subtype="html"  # Specify the subtype as HTML
    )

    # Initialize FastMail with your email configuration
    fm = FastMail(conf)

    # Send the email
    await fm.send_message(message)

    return {"message": "Emails sent successfully!"}


'''async def send_invitation_email():
    recipients = [
	"sudheerdumpala45@gmail.com",
    ]
    message = MessageSchema(
        subject="API Documentation Invitation",
        recipients=recipients,
        body="""
        Hello,

        We are excited to invite you to view our User Management API documentation on ReDoc.
        You can access the documentation by clicking the button below:

        [View API Documentation](http://54.80.159.115:8000/docs)

        Thank you,
        Your Team
        """,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
'''
