import asyncio
from telegram import Bot

async def main():
    bot = Bot(token='7876251352:AAFKOTc0uAvj_cpsK4dB6TwFEVjAtkJ0q9s')
    me = await bot.get_me()
    print(me)

asyncio.run(main())
