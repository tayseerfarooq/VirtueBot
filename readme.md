# 🕋 VirtueBot – Islamic Emotional Support Bot 🤖

[![Deploy on Railway](https://img.shields.io/badge/Deployed%20on-Railway-green?logo=railway)](https://railway.app)
[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-lightgrey.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4-orange.svg)](https://openai.com/)
[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-%E2%98%95-yellow?style=flat-square&logo=buy-me-a-coffee&logoColor=white&labelColor=black&color=FFDD00)](https://buymeacoffee.com/tayseerfarooq)

VirtueBot is an AI-powered Telegram bot that provides **Islamic emotional support and spiritual reflection**. It uses GPT to return verses from the Qur'an, stories from the life of Prophet Muhammad ﷺ, and practical advice — all with empathy and authenticity.

---

## 🌐 Live Telegram Bot

👉 [Click to Chat with VirtueBot](https://t.me/islambuddybot)

---

## 🧠 Features

- 📖 **Qur'anic verses** with **Surah & Ayah** references
- 🌟 **Seerah moments** from the life of Prophet Muhammad ﷺ
- 💬 **Practical Islamic advice** (prayer, dhikr, breathing exercises)
- 🤖 **Powered by OpenAI GPT-4-Turbo** for intelligent responses
- 📱 **Connected to Telegram** via Flask Webhooks
- ☁️ **Deployed on Railway** (no server maintenance!)
- 🔒 **Secure environment variable** management
- ⚡ **Real-time responses** with empathetic tone

---

## 🛠 Tech Stack

| Component | Technology |
|-----------|------------|
| **Backend** | Python + Flask |
| **AI Engine** | OpenAI GPT-4 (`openai` SDK) |
| **Messaging** | Telegram Bot API (`requests`) |
| **Hosting** | Railway.app |
| **Environment** | `.env` for secret management |
| **WSGI Server** | Gunicorn for production |

---

## 🚀 Getting Started

### 📦 Prerequisites

- **Python 3.10+**
- A [Telegram Bot Token](https://t.me/botfather) (free)
- An [OpenAI API Key](https://platform.openai.com/) (requires credits)
- A [Railway account](https://railway.app) (free tier available)

---

### 🔧 Local Development Setup

```bash
# 1. Clone the repository
git clone https://github.com/tayseerfarooq/VirtueBot.git
cd VirtueBot

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create environment file
touch .env
```

**Add to your `.env` file:**
```env
BOT_TOKEN=your_telegram_bot_token_here
OPENAI_API_KEY=your_openai_api_key_here
```

**Run the app locally:**
```bash
python app.py
```

**Expose locally using ngrok:**
```bash
ngrok http 8000
```

**Set the webhook:**
```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://<your-ngrok-url>/webhook"
```

---

### ☁️ Production Deployment (Railway)

1. **Push your code to GitHub**
2. **Go to [railway.app](https://railway.app)**
3. **New Project → Deploy from GitHub Repo**
4. **Add environment variables:**
   - `BOT_TOKEN=your_token_here`
   - `OPENAI_API_KEY=your_api_key_here`
5. **Set start command:**
   ```bash
   gunicorn app:app
   ```
6. **After deployment, set your webhook:**
   ```bash
   curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://<your-railway-url>/webhook"
   ```

---

## 🧪 Common Errors & Fixes I went through

| 🔥 Problem | ✅ Solution |
|------------|-------------|
| `OpenAIError: api_key must be set` | Add `OPENAI_API_KEY` to environment variables |
| `500 Internal Server Error` | Check OpenAI key or model name |
| `404 from Telegram` | Invalid bot token or malformed webhook |
| `Flask port already in use` | Kill process: `lsof -i :8000 && kill <PID>` |
| `gpt-4.1-nano not found` | Use correct model: `"gpt-4-turbo"` |
| `Git push rejected` | Run `git pull origin main` first |
| `ModuleNotFoundError` | Install dependencies: `pip install -r requirements.txt` |

---

## 📌 Example Conversations

### Example 1: Feeling Anxious
**User:** "I'm feeling very lost and anxious today"

**VirtueBot:**
```
📖 "And whoever relies upon Allah – then He is sufficient for him." (Surah At-Talaq 65:3)

🌟 During difficult times, the Prophet ﷺ would turn to prayer and tawakkul (trust in Allah). He taught us that when we feel overwhelmed, we should seek refuge in Allah and remember that He is always near.

💡 Try this: Take 3 deep breaths, say "Astaghfirullah" 3 times, and make dua. Allah hears every whisper of your heart.
```

### Example 2: Seeking Guidance
**User:** "I'm struggling with a difficult decision"

**VirtueBot:**
```
📖 "And consult them in the matter. And when you have decided, then rely upon Allah." (Surah Al-Imran 3:159)

🌟 The Prophet ﷺ always sought counsel from his companions before making important decisions. He taught us the value of istikhara (seeking Allah's guidance) and consultation.

💡 Make istikhara prayer, consult trusted people, and trust Allah's plan for you.
```

---

## 📒 Future Enhancements

- [ ] **Emotion journaling** - Save & view past reflections
- [ ] **Voice message support** - Whisper integration for audio
- [ ] **Feedback system** - "Was this helpful?" buttons
- [ ] **Admin dashboard** - Analytics and user insights
- [ ] **Multi-language support** - Arabic, Urdu, English
- [ ] **Daily Islamic reminders** - Scheduled spiritual messages
- [ ] **Quran recitation** - Audio verses integration
- [ ] **Prayer time integration** - Local prayer schedules

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Areas for Improvement
- **Accuracy of Quran/Seerah citations**
- **UX/UI flow optimization**
- **Hosting integrations**
- **Code documentation**
- **Testing and bug fixes**
- **Optimise the usage of tokens**

### Contribution Guidelines
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 🧕 Who This Is For

- **Muslims seeking emotional clarity** and spiritual guidance
- **Tech-savvy Muslims** building Islamic tools and applications
- **Developers learning** API integration, OpenAI, and cloud deployment
- **Anyone interested** in AI-powered spiritual support
- **Islamic organizations** looking to provide digital spiritual care

---

## 🛡 Disclaimer

This bot is an **AI tool for support and reflection**, **not a replacement for scholars, imams, or licensed therapists**. Always consult qualified religious authorities for serious matters and seek professional help when needed.

---

## 👨‍💻 Built by

**Tayseer Mohammed Farooq**  
📫 [tayseer.farooq69@gmail.com](mailto:tayseer.farooq69@gmail.com)  
🌐 [GitHub](https://github.com/tayseerfarooq)

---

## ☕ Support My Work

If this project helped you or brought benefit to your spiritual journey:

[![Buy Me A Coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee-%E2%98%95-yellow?style=flat-square&logo=buy-me-a-coffee&logoColor=white&labelColor=black&color=FFDD00)](https://buymeacoffee.com/tayseerfarooq)

Your support helps maintain and improve this project! 🙏

---

## 🌟 Star the Repo!

If you found this useful, please ⭐ the repo. It helps others discover the project and shows your support!

[![GitHub stars](https://img.shields.io/github/stars/tayseerfarooq/VirtueBot?style=social)](https://github.com/tayseerfarooq/VirtueBot)


---

## 🔗 Quick Links

- [Telegram Bot](https://t.me/islambuddybot)
- [GitHub Repository](https://github.com/tayseerfarooq/VirtueBot)
- [Railway Deployment](https://railway.app)
- [OpenAI Platform](https://platform.openai.com/)
- [Telegram BotFather](https://t.me/botfather)

---

*Made with ❤️ for the Muslim community* 