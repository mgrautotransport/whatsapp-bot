from flask import Flask, request, Response
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running"

@app.route("/webhook", methods=["POST"])
def webhook():
    return Response(
        """<?xml version="1.0" encoding="UTF-8"?>
<Response>
<Message>Hello from Railway WhatsApp bot!</Message>
</Response>""",
        mimetype="text/xml"
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
