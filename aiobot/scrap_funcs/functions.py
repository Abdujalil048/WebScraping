import requests
from bs4 import BeautifulSoup


def get_site(url):
    response = requests.get(url)
    return BeautifulSoup(response.text, 'html.parser')


# lnn = 'Top Growth Stocks for April 202'
# url = 'https://www.investopedia.com/'
#
#
# @dp.message_handler(commands=['start'])
# async def send_welcome(message: types.Message):
#     global lnn
#     site = get_site(url)
#     last_news = site.find('a', id="mntl-card-list-items_1-0")
#     while True:
#         if lnn != last_news.find('span', class_="card__title-text").text:
#             lnn = last_news.find('span', class_="card__title-text").text
#             news_page = get_site(last_news['href'])
#             news_header = news_page.find('h1', id="article-heading_2-0").text
#             news_about = translate(news_page.find("p", id="article-subheading_1-0").text,
#                                    "uz") + "\n\n" if news_page.find("p",
#                                                                     id="article-subheading_1-0") else ""
#             post_message = f'<b>{translate(news_header, "uz")}</b>\n\n{news_about}Batafsil: {last_news["href"]}'
#             news_photo = news_page.find('img', sizes="750px")['src']
#
#             await aiobot.send_photo(channel_id, news_photo, post_message, 'HTML')
#             await message.answer_photo(news_photo, post_message, 'HTML')
#             print('New post: ' + translate(news_header, 'uz'))
#             logging.info('New post: ' + translate(news_header, 'uz'))
#         sleep(60)
#         logging.info('1 minute. Last news: ' + last_news.find('span', class_="card__title-text").text)
