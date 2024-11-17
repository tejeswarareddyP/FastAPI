import smtplib

SMTP_SERVER = "smtp.gmail.com"  # or "smtp.gmail.com"
SMTP_PORT = 587  # or 465 for SSL
USERNAME = "tpeddireddy007@gmail.com"
PASSWORD = "ratqurhtxryhkvtb"

try:
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
    server.starttls()  # Start TLS encryption
    server.login(USERNAME, PASSWORD)
    print("Login successful! SMTP credentials are valid.")
    server.quit()
except Exception as e:
    print(f"Error: {e}")

