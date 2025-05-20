from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject, Update

from bot.bot_logger import BotEventLogger


class LoggingMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any],
    ) -> Any:
        real_event = event.message or event.callback_query
        if real_event and hasattr(real_event, "from_user"):
            data["bot_logger"] = BotEventLogger(
                user_id=real_event.from_user.id,
                full_name=real_event.from_user.full_name,
            )
        return await handler(event, data)
