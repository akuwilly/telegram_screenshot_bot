import asyncio
from telegram import Bot

async def main():
    bot = Bot(token='7876251352:AAFKOTc0uAvj_cpsK4dB6TwFEVjAtkJ0q9s')  # Token kamu
    updates = await bot.get_updates()

    for u in updates:
        chat = u.message.chat
        print("💬 Nama:", chat.first_name)
        print("🆔 Chat ID:", chat.id)
        print("📨 Pesan:", u.message.text)
        print("---------")

asyncio.run(main())
