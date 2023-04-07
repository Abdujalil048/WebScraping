from aiogram.types import Message, ParseMode
from aiogram.utils.markdown import bold

from aiobot.dispatcher import dis


@dis.message_handler(commands='start')
async def start_process(msg: Message):
    text = bold('Process started !')
    await msg.answer(text, ParseMode.MARKDOWN_V2)
