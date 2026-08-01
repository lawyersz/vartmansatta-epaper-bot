from telegram import Bot
from config import TELEGRAM_BOT_TOKEN
import asyncio


async def test_connection():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    me = await bot.get_me()

    print("===================================")
    print("Telegram Bot Connected Successfully")
    print("===================================")
    print(f"Bot Name : {me.first_name}")
    print(f"Username : @{me.username}")


if __name__ == "__main__":
    asyncio.run(test_connection())
