from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

# سيرفر التجربة الأساسي
SERVER = "http://fortv.cc:8080"
USER = "1A63fh"
PASS = "337373"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/content')
def get_content():
    # نأخذ نوع المحتوى من المتصفح (vod_streams أو series أو live_streams)
    action = request.args.get('type', 'get_vod_streams')
    url = f"{SERVER}/player_api.php?username={USER}&password={PASS}&action={action}"
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=25)
        # نرسل أول 60 عنصر فقط لضمان السرعة في البداية
        return jsonify(response.json()[:60])
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
