from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "Bot is running", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    return """<?xml version="1.0" encoding="UTF-8"?>
<Response><Message>Hello from Railway</Message></Response>""", 200, {"Content-Type": "text/xml"}

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
