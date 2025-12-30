from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

# الرابط العالمي الجديد (يمكنك استبدال <FILENAME> بـ index أو countries/ar)
M3U_URL = "https://iptv-org.github.io/iptv/index.m3u"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/channels')
def get_channels():
    try:
        # جلب البيانات مع تحديد متصفح وهمي لتجنب الحظر
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(M3U_URL, headers=headers, timeout=15)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}", 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
