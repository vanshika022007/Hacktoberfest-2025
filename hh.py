"""
📧 Email Sender Script
----------------------
Author: Open for Hacktoberfest 2025 💻
Maintainer: @milansinghal2004
License: MIT

This script allows you to send emails (plain or HTML) to multiple recipients with optional CC/BCC
and file attachments. It logs all email activity and errors in a log file.

✅ Features:
- Send to multiple recipients, CC, and BCC
- Supports plain text and HTML body
- Allows multiple attachments
- Logs all email activity
- Safe with environment variable password option
- Auto retry for failed deliveries
"""

import smtplib
import os
import datetime
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# ------------------ CONFIGURATION ------------------
LOG_FILE = "email_log.txt"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
MAX_RETRIES = 3


def log_message(message: str):
    """Append a log entry with a timestamp to email_log.txt."""
    with open(LOG_FILE, "a", encoding="utf-8") as log:
        log.write(f"[{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {message}\n")


def send_email(sender, password, to_emails, cc_emails, bcc_emails, subject, body, body_type, attachments):
    """Send an email with given parameters and handle SMTP connection."""
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = ", ".join(to_emails)
    msg["CC"] = ", ".join(cc_emails)
    msg["Subject"] = subject

    # Attach email body
    msg.attach(MIMEText(body, "html" if body_type == "2" else "plain"))

    # Attach files
    for f in attachments:
        try:
            with open(f, "rb") as file:
                part = MIMEApplication(file.read(), Name=os.path.basename(f))
            part["Content-Disposition"] = f'attachment; filename="{os.path.basename(f)}"'
            msg.attach(part)
            print(f"📎 Attached: {f}")
        except Exception as e:
            print(f"⚠️ Failed to attach {f}: {e}")
            log_message(f"Attachment failed: {f} — {e}")

    # Combine all recipients
    all_recipients = [email.strip() for email in to_emails + cc_emails + bcc_emails if email.strip()]

    # Try sending with retry logic
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()
                server.login(sender, password)
                server.sendmail(sender, all_recipients, msg.as_string())

            print("✅ Email sent successfully!")
            log_message(f"Email sent — Subject: '{subject}' | To: {all_recipients}")
            return
        except Exception as e:
            print(f"❌ Attempt {attempt}: Failed to send email. Error: {e}")
            log_message(f"Send failed (Attempt {attempt}): {e}")
            time.sleep(2)

    print("🚫 Email could not be sent after multiple attempts.")
    log_message("Email failed after maximum retries.")


def main():
    """Main interactive flow for sending emails."""
    print("\n📨 --- Hacktoberfest 2025 Email Sender --- 🧑‍💻")
    print("Send secure, formatted emails with attachments!\n")

    # Input details
    sender_email = input("Enter your Gmail address: ").strip()

    # Option for password via environment variable for security
    use_env = input("Use environment variable for password? (y/n): ").lower()
    if use_env == "y":
        password = os.getenv("EMAIL_PASSWORD")
        if not password:
            print("⚠️ EMAIL_PASSWORD not found in environment. Please set it or enter manually.")
            password = input("Enter your Gmail app password: ").strip()
    else:
        password = input("Enter your Gmail app password: ").strip()

    to_emails = input("Enter recipient emails (comma-separated): ").split(",")
    cc_emails = input("Enter CC emails (comma-separated, leave blank if none): ").split(",") if input("Add CC? (y/n): ").lower() == "y" else []
    bcc_emails = input("Enter BCC emails (comma-separated, leave blank if none): ").split(",") if input("Add BCC? (y/n): ").lower() == "y" else []

    subject = input("Enter subject line: ").strip()
    body_type = input("Email type? (1 = Plain Text | 2 = HTML): ").strip()
    body = input("Enter your email message (HTML supported if chosen): ").strip()

    # Handle attachments
    attachments = []
    while True:
        file_path = input("Enter attachment path (or leave blank to stop): ").strip()
        if not file_path:
            break
        if os.path.exists(file_path):
            attachments.append(file_path)
        else:
            print("⚠️ File not found, please check the path.")

    # Confirm details
    print("\n📦 Summary:")
    print(f"From: {sender_email}")
    print(f"To: {to_emails}")
    print(f"CC: {cc_emails}")
    print(f"BCC: {bcc_emails}")
    print(f"Subject: {subject}")
    print(f"Attachments: {attachments if attachments else 'None'}")

    confirm = input("\nSend this email? (y/n): ").lower()
    if confirm == "y":
        send_email(sender_email, password, to_emails, cc_emails, bcc_emails, subject, body, body_type, attachments)
    else:
        print("❌ Email canceled by user.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Process interrupted by user.")
        log_message("User interrupted execution.")
    except Exception as e:
        print(f"🚨 Unexpected error: {e}")
        log_message(f"Unexpected error: {e}")
