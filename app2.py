from flask import Flask, jsonify, render_template_string
import socket, os
app = Flask(__name__)

HTML = """<h1 style='color:#4a5bdc;'>Kapruka DevOps – Assignment 2</h1>
<p>Hostname: {{h}}</p><p>Environment: {{e}}</p><p>Status: ✅ Running</p>"""

@app.route("/")
def home():
    return render_template_string(HTML, h=socket.gethostname(), e=os.getenv("ENVIRONMENT","Production"))

@app.route("/health")
def health():
    return jsonify(status="healthy", service="kapruka-ecommerce", version="1.0.0")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
