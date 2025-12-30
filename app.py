from flask import Flask, render_template, request, jsonify
import os

app = Flask(__name__)

# قاعدة بيانات وهمية (سيتم حفظ المستخدمين في ذاكرة السيرفر مؤقتاً)
# في التطور القادم سنربطها بـ Database حقيقية
registered_users = []

@app.route('/')
def index():
    # عرض الواجهة الاحترافية التي صممناها
    return render_template('register.html')

@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.json
        phone = data.get('phone')
        password = data.get('password')
        
        # حماية إضافية: التحقق من الرقم في السيرفر
        if not phone.startswith(('05', '06', '07')) or len(phone) != 10:
            return jsonify({"status": "error", "message": "عذراً! الرقم غير جزائري"}), 400

        # حفظ المستخدم (MisterAI Security)
        registered_users.append({"phone": phone, "status": "active"})
        print(f"New User Joined: {phone}")
        
        return jsonify({"status": "success", "message": "أهلاً بك في عائلتنا! تم تأمين حسابك بنجاح."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
