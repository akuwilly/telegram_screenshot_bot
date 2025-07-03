import asyncio
import schedule
import time
import os
from telegram import Bot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import datetime

# === CONFIG FROM ENV ===
TOKEN = os.environ['TELEGRAM_BOT_TOKEN']
CHAT_ID = int(os.environ['TELEGRAM_CHAT_ID'])
URL_WEBSITE = os.environ.get('TARGET_URL', 'https://www.google.com')

# === Driver path in container ===
CHROMEDRIVER_PATH = '/usr/bin/chromedriver'
CHROME_BIN = '/usr/bin/google-chrome'

bot = Bot(token=TOKEN)

async def ambil_dan_kirim_screenshot():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280,720')
    options.binary_location = CHROME_BIN

    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.set_page_load_timeout(30)
        driver.get(URL_WEBSITE)
    except Exception as e:
        print(f"⚠️ Timeout saat loading: {e}")

    time.sleep(3)
    filename = 'screenshot.png'
    driver.save_screenshot(filename)
    driver.quit()

    waktu = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
    caption = f'Screenshot otomatis - {waktu}'

    with open(filename, 'rb') as foto:
        await bot.send_photo(chat_id=CHAT_ID, photo=foto, caption=caption)

    print(f"[{waktu}] Screenshot otomatis berhasil dikirim.")

def job():
    asyncio.run(ambil_dan_kirim_screenshot())

# Jadwal
schedule.every().day.at("07:00").do(job)
schedule.every().day.at("09:00").do(job)
schedule.every().day.at("13:00").do(job)
schedule.every().day.at("15:00").do(job)
schedule.every().day.at("17:00").do(job)
schedule.every().day.at("20:00").do(job)

print("📡 BOT JALAN ✅ Menunggu waktu kirim...")

while True:
    schedule.run_pending()
    time.sleep(1)
