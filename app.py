from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "ربات روی سرور فعال است!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    
    # پاسخ فرضی (اینجا میشه NLP یا اتصال به ویکیپدیا گذاشت)
    bot_reply = f"شما گفتید: {user_message}"
    
    return jsonify({'reply': bot_reply})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
