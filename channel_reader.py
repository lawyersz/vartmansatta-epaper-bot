import asyncio
from telegram import Bot
from config import TELEGRAM_BOT_TOKEN


async def get_updates():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    updates = await bot.get_updates()

    print("========== UPDATES ==========")

    if not updates:
        print("No updates found.")
        return

    for update in updates:
        print(update)


if __name__ == "__main__":
    asyncio.run(get_updates())
