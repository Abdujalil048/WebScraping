from logging import basicConfig
from dotenv import load_dotenv
from logger import log_config


def start_polling():
    import aiobot
    import aiogram
    aiogram.executor.start_polling(aiobot.dispatcher.dis, skip_updates=True)


if __name__ == '__main__':
    basicConfig(**log_config)
    load_dotenv()
    start_polling()
