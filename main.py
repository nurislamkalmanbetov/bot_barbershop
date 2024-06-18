from config import TOKEN
import asyncio
from aiogram import Bot, Dispatcher
from handlers.commands import router

from database.models import models_main

import logging
import sys



async def main():

    bot = Bot(token=TOKEN) # Подключает 
    dp = Dispatcher()
    dp.include_router(router=router)

    await dp.start_polling(bot) # запускает бота в активном состоянии
    # await models_main() # для добавления баз данных


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO,stream=sys.stdout)

    try:
        asyncio.run(main())
    except Exception as e:
        print("Ошибка",e)
