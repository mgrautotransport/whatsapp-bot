from flask import Flask, request, Response
from openai import OpenAI
import os

app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route("/", methods=["GET"])
def home():
    return "Bot is running", 200

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        incoming_msg = request.form.get("Body", "")

        response = client.responses.create(
            model="gpt-4.1",
            input=f"User says: {incoming_msg}. Reply like a helpful WhatsApp assistant and ask one follow-up question."
        )

        reply = response.output_text.strip()

        twiml = f"""<?xml version="1.0" encoding="UTF-8"?>
<Response><Message>{reply}</Message></Response>"""

        return Response(twiml, mimetype="text/xml")
    except Exception as e:
        print("ERROR:", str(e))
        return Response(
            """<?xml version="1.0" encoding="UTF-8"?>
<Response><Message>Sorry, the bot hit an error.</Message></Response>""",
            mimetype="text/xml",
            status=200,
        )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
