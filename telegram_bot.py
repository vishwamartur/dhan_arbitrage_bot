import os
from telegram import Bot
from telegram.error import TelegramError

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

class TelegramBot:
    def __init__(self):
        if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
            print("Warning: TELEGRAM_BOT_TOKEN or TELEGRAM_CHAT_ID environment variables are not set. Telegram notifications will be disabled.")
            self.bot = None
        else:
            self.bot = Bot(token=TELEGRAM_BOT_TOKEN)
            self.chat_id = TELEGRAM_CHAT_ID

    async def send_message(self, message):
        if self.bot:
            try:
                await self.bot.send_message(chat_id=self.chat_id, text=message)
                print(f"Telegram message sent: {message}")
            except TelegramError as e:
                print(f"Error sending Telegram message: {e}")
        else:
            print(f"Telegram bot not initialized. Message not sent: {message}")

    async def send_photo(self, photo_path, caption=None):
        if self.bot:
            try:
                with open(photo_path, 'rb') as photo:
                    await self.bot.send_photo(chat_id=self.chat_id, photo=photo, caption=caption)
                print(f"Telegram photo sent: {photo_path}")
            except TelegramError as e:
                print(f"Error sending Telegram photo: {e}")
        else:
            print(f"Telegram bot not initialized. Photo not sent: {photo_path}")

# Example usage (for testing purposes)
# if __name__ == "__main__":
#     import asyncio
#     # Set environment variables before running this script
#     # export TELEGRAM_BOT_TOKEN="your_bot_token"
#     # export TELEGRAM_CHAT_ID="your_chat_id"

#     async def main():
#         bot = TelegramBot()
#         await bot.send_message("Hello from your Dhan Arbitrage Bot!")
#         # await bot.send_photo("path/to/your/image.png", "This is a test image.")

#     asyncio.run(main())


