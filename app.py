import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import Config, load_config

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

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
