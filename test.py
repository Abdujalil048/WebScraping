from mtranslate import translate

news_header = "JXN, AMBC, and WDH are top for value, growth, and momentum, respectively"
uz_translation = translate(news_header, 'uz')
print(uz_translation)