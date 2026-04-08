import sys
import asyncio
import logging
from wikilib import basic_search

from decouple import config
from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, Router, types, filters, html

TOKEN = config('TG_BOT_TOKEN')

router = Router()
dp = Dispatcher()
dp.include_router(router)

@dp.message(filters.CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f'Hello {html.bold(message.from_user.full_name)}!')

"""
@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")
"""

@router.message(filters.Command("search"))
async def command_search_handler(message: types.Message) -> None:
    result = basic_search(message.text)
    await message.answer(result)

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

