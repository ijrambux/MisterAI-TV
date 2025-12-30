from flask import Flask, render_template, requests
import os

app = Flask(__name__)

# الرابط الجديد الذي أرسلته
M3U_URL = "https://raw.githubusercontent.com/hemzaberkane/ARAB-IPTV/refs/heads/main/ARABIPTV.m3u"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/channels')
def get_channels():
    try:
        response = requests.get(M3U_URL)
        # هنا نقوم بإرسال النص كما هو والمتصفح سيتولى الباقي لسرعة الأداء
        return response.text
    except:
        return ""

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
