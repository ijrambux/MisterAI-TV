from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

XTREAM_SERVERS = [
    "http://fortv.cc:8080/get.php?username=1A63fh&password=337373&type=m3u",
    "http://tvhomesmart.xyz:8080/get.php?username=32930499&password=5req2f3q3&type=m3u_plus",
    "http://mytvstream.net:8080/get.php?username=TWEk66&password=036939&type=m3u_plus",
    "http://lobitv65.xyz:8080/get.php?username=svd2884&password=svd.475&type=m3u_plus",
    "http://fruhd.cc:80/get.php?username=4428202673895240&password=4428202673895240&type=m3u_plus"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/servers')
def get_servers():
    return jsonify({"servers": XTREAM_SERVERS})

@app.route('/api/proxy')
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return "Missing URL", 400
    try:
        # Render سيرفر حقيقي، لذا يمكننا زيادة وقت الانتظار قليلاً لجلب قنوات أكثر
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        response = requests.get(target_url, headers=headers, timeout=25)
        return response.text
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    # Render يمرر رقم البورت عبر متغيرات البيئة
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
