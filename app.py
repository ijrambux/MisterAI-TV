from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests

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
    """هذه الدالة تجلب محتوى الـ M3U نيابة عن المتصفح لتجنب حظر HTTP"""
    target_url = request.args.get('url')
    try:
        response = requests.get(target_url, timeout=10)
        return response.text
    except:
        return "خطأ في جلب البيانات", 500

if __name__ == '__main__':
    app.run()
