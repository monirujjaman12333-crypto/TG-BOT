import subprocess
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"OK")
    def log_message(self, *args):
        pass  # log বন্ধ রাখো

def run_server():
    HTTPServer(("0.0.0.0", 8000), HealthHandler).serve_forever()

# Health check server background এ চালাও
threading.Thread(target=run_server, daemon=True).start()

# বাকি bot চালাও
subprocess.Popen(["python", "bot.py"])
subprocess.Popen(["python", "otp_monitor.py"])

while True:
    pass
