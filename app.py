from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

SERVER = "http://fortv.cc:8080"
USER = "1A63fh"
PASS = "337373"

# مخزن مؤقت لتقليل الضغط على السيرفر
cache = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/content')
def get_content():
    action = request.args.get('type', 'get_live_streams')
    
    # إذا كانت البيانات موجودة في الذاكرة، أرسلها فوراً
    if action in cache:
        return jsonify(cache[action])

    url = f"{SERVER}/player_api.php?username={USER}&password={PASS}&action={action}"
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        # تقليل حجم البيانات المرسلة للمتصفح (أول 200 عنصر فقط للسرعة القصوى)
        short_data = data[:200]
        cache[action] = short_data
        return jsonify(short_data)
    except:
        return jsonify([])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
