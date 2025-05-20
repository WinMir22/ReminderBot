import logging
from dataclasses import dataclass

logger = logging.getLogger(__name__)


@dataclass
class BotEventLogger:
    user_id: int
    full_name: str

    def start_logger(self):
        logger.info(f"Пользователь {self.full_name}({self.user_id}) запустил бота.")
