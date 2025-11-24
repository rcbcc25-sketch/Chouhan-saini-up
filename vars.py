#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "29731917"))
API_HASH = environ.get("API_HASH", "d0b73a75f2d12cae5b04c21044ff0148")
BOT_TOKEN = environ.get("BOT_TOKEN", "8095089104:AAEDDTaYEufuhzvz1cBsbTA0TtxIr7FaPAk")

OWNER = int(environ.get("OWNER", "8050673236"))
CREDIT = environ.get("CREDIT", "[꧁༒☬🦋✨⚔️MR.𝐂𝐡𝐨𝐮𝐡𝐚𝐧⚔️✨🦋☬༒꧂](tg://openmessage?user_id=8050673236)"

TOTAL_USER = os.environ.get('TOTAL_USERS', '8050673236').split(',')
TOTAL_USERS = [int(user_id) for user_id in TOTAL_USER]

AUTH_USER = os.environ.get('AUTH_USERS', '8050673236').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set


