from aiogram import Bot
import os

TOKEN = os.getenv('API_TOKEN')
Bot = Bot(TOKEN)
