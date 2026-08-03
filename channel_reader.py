import asyncio
import os

from telegram import Bot
from config import TELEGRAM_BOT_TOKEN, DOWNLOAD_FOLDER


async def get_updates():
    bot = Bot(token=TELEGRAM_BOT_TOKEN)

    updates = await bot.get_updates()

    if not updates:
        print("No updates found.")
        return

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    for update in updates:

        if update.channel_post and update.channel_post.document:

            document = update.channel_post.document

            print(f"Found PDF: {document.file_name}")

            telegram_file = await bot.get_file(document.file_id)

            save_path = os.path.join(
                DOWNLOAD_FOLDER,
                document.file_name
            )

            await telegram_file.download_to_drive(save_path)

            print(f"Downloaded successfully: {save_path}")


if __name__ == "__main__":
    asyncio.run(get_updates())
