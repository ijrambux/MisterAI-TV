from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# رابط القنوات العربية من GitHub
M3U_URL = "https://raw.githubusercontent.com/hemzaberkane/ARAB-IPTV/refs/heads/main/ARABIPTV.m3u"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/channels')
def get_channels():
    try:
        # تحديد وقت انتظار لضمان عدم تعليق السيرفر
        response = requests.get(M3U_URL, timeout=15)
        return response.text
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
