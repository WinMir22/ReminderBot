from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.bot.bot_logger import BotEventLogger

router = Router()


@router.message(CommandStart())
async def start_command(message: Message, bot_logger: BotEventLogger):
    await message.answer(
        "Привет! Я бот для напоминаний. Выберите одно из действий ниже"
    )
    await message.delete()
    bot_logger.start_logger()
