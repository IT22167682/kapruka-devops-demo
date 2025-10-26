from flask import Flask, render_template_string
import socket
import os

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Kapruka E-Commerce Platform</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            display: flex;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
        }
        .container {
            background: white;
            padding: 50px;
            border-radius: 15px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.3);
            text-align: center;
            max-width: 600px;
        }
        h1 {
            color: #667eea;
            margin-bottom: 10px;
            font-size: 2.5em;
        }
        .subtitle {
            color: #666;
            font-size: 1.2em;
            margin-bottom: 30px;
        }
        .info-box {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
        }
        .info-item {
            margin: 10px 0;
            font-size: 1.1em;
        }
        .label {
            font-weight: bold;
            color: #667eea;
        }
        .value {
            color: #333;
        }
        .status {
            display: inline-block;
            padding: 8px 20px;
            background: #28a745;
            color: white;
            border-radius: 20px;
            margin-top: 20px;
            font-weight: bold;
        }
        .badge {
            display: inline-block;
            padding: 5px 15px;
            background: #764ba2;
            color: white;
            border-radius: 15px;
            font-size: 0.9em;
            margin: 5px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🛒 Kapruka Holdings PLC</h1>
        <p class="subtitle">E-Commerce Platform - DevOps Implementation</p>
        
        <div class="info-box">
            <div class="info-item">
                <span class="label">Container ID:</span>
                <span class="value">{{ hostname }}</span>
            </div>
            <div class="info-item">
                <span class="label">Environment:</span>
                <span class="value">{{ environment }}</span>
            </div>
            <div class="info-item">
                <span class="label">Version:</span>
                <span class="value">v1.0.0</span>
            </div>
        </div>
        
        <div class="status">✓ System Operational</div>
        
        <div style="margin-top: 30px;">
            <span class="badge">Jenkins CI/CD</span>
            <span class="badge">Docker Containerized</span>
            <span class="badge">ISO Compliant</span>
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    hostname = socket.gethostname()
    environment = os.getenv('ENVIRONMENT', 'Production')
    return render_template_string(HTML_TEMPLATE, hostname=hostname, environment=environment)

@app.route('/health')
def health():
    return {
        'status': 'healthy',
        'service': 'kapruka-ecommerce',
        'version': '1.0.0'
    }, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000, debug=False)


