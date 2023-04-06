from time import sleep

from functions import get_site
from mtranslate import translate
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6117395006:AAGA23nlzBzpA-tUZtmEw6GMcU17-xoSYYM'
lnn = 'Top Growth Stocks for April 202'
url = 'https://www.investopedia.com/'
channel_id = -1001975777742


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s (%(filename)s:%(lineno)d)"

    FORMATS = {
        logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)

logging.basicConfig(level=logging.INFO, format='%(asctime)s | %(levelname)s | %(message)s',
                    datefmt='%m-%d-%Y %H:%M:%S')

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    global lnn
    site = get_site(url)
    last_news = site.find('a', id="mntl-card-list-items_1-0")
    while True:
        if lnn != last_news.find('span', class_="card__title-text").text:
            lnn = last_news.find('span', class_="card__title-text").text
            news_page = get_site(last_news['href'])
            news_header = news_page.find('h1', id="article-heading_2-0").text
            news_about = translate(news_page.find("p", id="article-subheading_1-0").text,
                                   "uz") + "\n\n" if news_page.find("p",
                                                                    id="article-subheading_1-0") else ""
            post_message = f'<b>{translate(news_header, "uz")}</b>\n\n{news_about}Batafsil: {last_news["href"]}'
            news_photo = news_page.find('img', sizes="750px")['src']

            await bot.send_photo(channel_id, news_photo, post_message, 'HTML')
            await message.answer_photo(news_photo, post_message, 'HTML')
            print('New post: ' + translate(news_header, 'uz'))
            logging.info('New post: ' + translate(news_header, 'uz'))
        sleep(60)
        logging.info('1 minute. Last news: '+last_news.find('span', class_="card__title-text").text)


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
