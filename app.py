import win32evtlog
import win32evtlogutil
import time
import os
from dotenv import load_dotenv
import smtplib
from email.mime.text import MIMEText

# Load environment variables from .env file
load_dotenv()

LOG_FILE = "alerts.log"
EMAIL_ALERTS_ENABLED = True

# Email configuration from .env
EMAIL_HOST = os.getenv("EMAIL_HOST")
EMAIL_PORT = int(os.getenv("EMAIL_PORT"))
EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASS = os.getenv("EMAIL_PASS")
EMAIL_TO = os.getenv("EMAIL_TO")


def send_email_alert(event_data):
    if not EMAIL_ALERTS_ENABLED:
        return

    subject = "🚨 Failed Login Alert Detected!"
    body = f"A failed login attempt was detected:\n\n{event_data}"
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_USER
    msg["To"] = EMAIL_TO

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USER, EMAIL_PASS)
            server.send_message(msg)
            print("[+] Email alert sent.")
    except Exception as e:
        print(f"[!] Failed to send email: {e}")


def log_to_file(data):
    with open(LOG_FILE, "a") as f:
        f.write(data + "\n")


def monitor_failed_logins():
    print("[*] Monitoring for failed logins (Event ID 4625)...\n")

    server = 'localhost'
    log_type = 'Security'
    hand = win32evtlog.OpenEventLog(server, log_type)
    flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

    seen_records = set()  # To avoid duplicates

    while True:
        events = win32evtlog.ReadEventLog(hand, flags, 0)
        if events:
            for event in events:
                if event.EventID == 4625:
                    record_id = event.RecordNumber
                    if record_id in seen_records:
                        continue  # Already processed

                    seen_records.add(record_id)
                    timestamp = event.TimeGenerated.Format()
                    source = event.SourceName
                    event_id = event.EventID
                    category = event.EventCategory
                    msg = win32evtlogutil.SafeFormatMessage(event, log_type)

                    event_data = f"[{timestamp}] Event ID: {event_id} | Source: {source} | Category: {category}\n{msg}"
                    print(event_data)
                    print("-" * 40)

                    log_to_file(event_data)
                    send_email_alert(event_data)
        time.sleep(5)


if __name__ == "__main__":
    monitor_failed_logins()
