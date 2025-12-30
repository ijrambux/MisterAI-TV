from flask import Flask, render_template, jsonify
import requests
import re

app = Flask(__name__)

# قائمة السيرفرات الكاملة التي زودتني بها
XTREAM_SERVERS = [
    "http://fortv.cc:8080/get.php?username=1A63fh&password=337373&type=m3u",
    "http://tvhomesmart.xyz:8080/get.php?username=32930499&password=5req2f3q3&type=m3u_plus",
    "http://mytvstream.net:8080/get.php?username=TWEk66&password=036939&type=m3u_plus",
    "http://lobitv65.xyz:8080/get.php?username=svd2884&password=svd.475&type=m3u_plus",
    "http://nuhygo.shop:8080/get.php?username=2643496sec&password=2643496sec&type=m3u_plus",
    "http://fruhd.cc:80/get.php?username=4428202673895240&password=4428202673895240&type=m3u_plus"
]

def parse_multi_m3u(urls):
    all_channels = []
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) IPTV-Pro'}
    
    for url in urls:
        try:
            response = requests.get(url, headers=headers, timeout=7)
            if response.status_code == 200:
                # استخراج الشعار، الاسم، والرابط
                matches = re.findall(r'#EXTINF:-1.*?tvg-logo="(.*?)".*?,(.*?)\n(http.*)', response.text)
                for logo, name, link in matches:
                    all_channels.append({
                        'name': name.strip(),
                        'logo': logo if logo else 'https://via.placeholder.com/150?text=TV',
                        'url': link.strip()
                    })
        except:
            continue
    return all_channels

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/load_all')
def load_all():
    # جلب القنوات من كافة السيرفرات (نأخذ أول 100 من كل سيرفر للسرعة)
    data = parse_multi_m3u(XTREAM_SERVERS)
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)