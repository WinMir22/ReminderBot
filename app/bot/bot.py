import logging

from aiogram import Bot, Dispatcher

from app.bot.config import Config, load_config
from app.bot.handlers import start
from app.bot.middlewares.LoggingMiddleware import LoggingMiddleware

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
        "[%(asctime)s] - %(name)s - %(message)s",
    )

    config: Config = load_config()

    bot = Bot(token=config.tg_bot.bot_token)
    dp = Dispatcher()

    dp.include_router(start.router)

    dp.update.middleware(LoggingMiddleware())

    await dp.start_polling(bot)
