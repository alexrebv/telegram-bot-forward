import os
import logging
import gspread
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from google.oauth2.service_account import Credentials
import asyncio

# Логирование
logging.basicConfig(level=logging.INFO)

# Загружаем токен
BOT_TOKEN = os.getenv("7954205733:AAFuZoteW2G1e8UtYmDvmNCc15sweideVdU")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Подключаем Google Sheets
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
credentials = Credentials.from_service_account_file(
    "credentials.json", scopes=SCOPES
)
gc = gspread.authorize(credentials)
sheet = gc.open_by_key(os.getenv("1J_Z2zHj4dRj6yaZR72IKQV5-hl1nkcTVmUgSRGz1NQk")).sheet1  # первая вкладка таблицы

@dp.message()
async def save_message(message: Message):
    """Сохраняем входящие сообщения в Google таблицу"""
    user = message.from_user.username or message.from_user.full_name
    text = message.text
    sheet.append_row([user, text])

    await message.answer("✅ Сообщение сохранено в Google Sheets")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
