import asyncio
import logging
from aiogram import Bot, Dispatcher
from api_token import Token

from routers import router as main_router
1

bot = Bot(Token)
dp = Dispatcher()
dp.include_router(main_router)


async def main():
    # logging.basicConfig(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)
    await bot.delete_webhook(drop_pending_updates=True)


if __name__ == "__main__":
    asyncio.run(main())
