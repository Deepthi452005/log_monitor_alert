from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    log_file = 'alerts.log'
    if os.path.exists(log_file):
        with open(log_file, 'r') as f:
            logs = f.readlines()
    else:
        logs = ["No failed login attempts logged yet."]
    return render_template('dashboard.html', logs=logs)

if __name__ == '__main__':
    app.run(debug=True)
