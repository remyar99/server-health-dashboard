from flask import Flask
import psutil

app = Flask(__name__)

@app.route("/")
def home():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent
    return f"""
    <h1>Server Dashboard</h1>

    CPU: {cpu}%<br>
    Memory: {memory}%<br>
    Disk: {disk}%
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)


