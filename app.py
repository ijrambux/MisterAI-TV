from flask import Flask, render_template, jsonify, request
import requests
import re

app = Flask(__name__)

# قائمة السيرفرات التي قدمتها
SERVERS = [
    "http://fortv.cc:8080/get.php?username=1A63fh&password=337373&type=m3u",
    "http://tvhomesmart.xyz:8080/get.php?username=32930499&password=5req2f3q3&type=m3u_plus",
    "http://mytvstream.net:8080/get.php?username=TWEk66&password=036939&type=m3u_plus"
    # أضف البقية هنا
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/channels')
def get_channels():
    # جلب القنوات من سيرفر واحد في كل مرة لتقليل الضغط
    server_id = int(request.args.get('s', 0))
    if server_id >= len(SERVERS): return jsonify([])
    
    try:
        r = requests.get(SERVERS[server_id], timeout=5)
        # استخراج أول 50 قناة فقط لتسريع الاستجابة
        matches = re.findall(r'#EXTINF:-1.*?,(.*?)\n(http.*)', r.text)[:50]
        return jsonify([{"name": m[0], "url": m[1]} for m in matches])
    except:
        return jsonify([])

# مهم جداً لـ Vercel
app.debug = False
