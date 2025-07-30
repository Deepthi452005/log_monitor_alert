# 🛡️ Log Monitoring & Alerting System (Windows)

A Python-based log monitoring and alerting tool for Windows Security Event Logs.  
It detects failed login attempts (`Event ID 4625`), logs them locally, sends email alerts for critical events, and displays them in a web-based dashboard using Flask.

---

## 🚀 Features

- ✅ Real-time monitoring of Windows Event Logs
- 📂 Local log storage (`alerts.log`)
- 📬 Email notifications for critical events
- 🌐 Flask-based web dashboard to view alerts
- 🔒 Useful for Blue Team/SOC mini-projects or Windows incident detection

---

## 🗂️ Project Structure

log_monitor_alert/
├── app.py # Main log monitoring script
├── dashboard.py # Flask web app to display alerts
├── .env # Environment variables (email settings)
├── requirements.txt # Required Python packages
├── alerts.log # Generated log file
└── templates/
└── dashboard.html # Web dashboard HTML
2. 🔐 Configure Email in .env
3. ▶️ Run Log Monitoring
4. 🌐 Run Web Dashboard

🧪 How to Test

Lock your PC
Try logging in with a wrong password
The event will be logged as Event ID 4625

It should:
Appear in the terminal
Be written to alerts.log
Send an email
Display in the Flask dashboard

🧰 Built With

Python
Flask
pywin32
dotenv

📚 Use Case

Beginner-friendly cybersecurity project
Windows security log monitoring
Blue team lab simulation
Real-time alerting system


📄 License
This project is licensed under the MIT License.

🙋‍♂️ Author
Deepu Deepthi
GitHub: @Deepthi452005





