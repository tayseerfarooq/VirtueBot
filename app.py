from flask import Flask, request
import requests
import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read your API keys from environment variables
BOT_TOKEN = os.getenv("BOT_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)
# Initialize Flask app
app = Flask(__name__)

# Initialize OpenAI client using new SDK style


# Define your webhook route - cleaner version, not using the full bot token in URL
@app.route("/webhook", methods=["POST"])
def webhook():
    print("✅ Webhook endpoint hit")
    # Parse incoming data from Telegram
    data = request.get_json()
    print("📥 Raw data received:", data)

    # Extract the message and chat ID
    if "message" in data:
        print("🧠 Telegram message found")
        user_message = data["message"].get("text", "")
        chat_id = data["message"]["chat"]["id"]
        print("💬 Message text:", user_message)
        print("👤 Chat ID:", chat_id)

        # If user sent a message, pass it to OpenAI for a response
        if user_message:
            print("🤖 Sending message to OpenAI...")
            # OpenAI call using new SDK style
            response = client.chat.completions.create(
                model="gpt-4.1-nano",
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are an Islamic emotional support assistant. "
                            "When a user shares how they're feeling, respond with: "
                            "1. A relevant verse from the Quran (include surah and ayah number), "
                            "2. A story or moment from the life of Prophet Muhammad ﷺ dealing with a similar feeling, "
                            "3. A short Islamic reminder or practical advice (e.g., prayer, dhikr, exercise). "
                            "DO NOT hallucinate; provide exact references. Keep tone empathetic and kind."
                        )
                    },
                    {"role": "user", "content": user_message}
                ]
            )

            # Extract the generated reply
            reply = response.choices[0].message.content.strip()
            print("✅ Response from OpenAI:", reply)

            # Send reply to user via Telegram
            send_telegram_message(chat_id, reply)

    return "ok", 200

# Function to send messages to Telegram
def send_telegram_message(chat_id, text):
    print(f"📢 Sending message with BOT_TOKEN: {BOT_TOKEN}")
    print("📤 Sending reply to Telegram:", text)
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": chat_id,
        "text": text,
        "parse_mode": "Markdown"
    }
    response = requests.post(url, json=payload)
    print("📬 Telegram API response:", response.json())

# Start the Flask server on port 8000 (or whatever is free)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
