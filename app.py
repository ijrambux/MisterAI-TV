from flask import Flask, render_template, request, Response
import requests
import os

app = Flask(__name__)

# الرابط العالمي المستقر الذي يدعم HTTPS
M3U_URL = "https://raw.githubusercontent.com/iptv-org/iptv/master/streams/ar.m3u"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/channels')
def get_channels():
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(M3U_URL, headers=headers, timeout=15)
        return Response(response.text, mimetype='text/plain')
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
