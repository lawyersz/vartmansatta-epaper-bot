from telegram import Bot
from config import TELEGRAM_BOT_TOKEN


def test_connection():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    me = bot.get_me()

    print(f"Connected successfully!")
    print(f"Bot Name : {me.first_name}")
    print(f"Username : @{me.username}")
