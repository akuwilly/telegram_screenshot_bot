import asyncio
from telegram import Bot
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time
import datetime

# === KONFIGURASI ===
TOKEN = '7876251352:AAFKOTc0uAvj_cpsK4dB6TwFEVjAtkJ0q9s'
CHAT_ID = 1276330579
URL_WEBSITE = 'https://www.google.com'
CHROMEDRIVER_PATH = r'E:\PKL\telegram_screenshot_bot\chromedriver-win64\chromedriver-win64\chromedriver.exe'

bot = Bot(token=TOKEN)

async def ambil_dan_kirim_screenshot():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    service = Service(CHROMEDRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        driver.set_window_size(1280, 720)
        driver.set_page_load_timeout(30)
        driver.get(URL_WEBSITE)
        time.sleep(5)


        filename = 'screenshot.png'
        driver.save_screenshot(filename)
        driver.quit()

        waktu = datetime.datetime.now().strftime('%d-%m-%Y %H:%M')
        caption = f'Screenshot otomatis dari dashboard - {waktu}'

        with open(filename, 'rb') as foto:
            await bot.send_photo(chat_id=CHAT_ID, photo=foto, caption=caption)

        print(f"[{waktu}] Screenshot berhasil dikirim ke Telegram.")

    except Exception as e:
        print("❌ Gagal:", e)
        driver.quit()

# Jalankan
asyncio.run(ambil_dan_kirim_screenshot())
