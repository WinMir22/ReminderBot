"""
Application configuration management.

Provides typed configuration classes and environment variables loading.
Designed to be imported as a module, not executed directly.

Example:
    >>> from config import load_config
    >>> config = load_config()

Environment variables:
    See individual class definitions (DatabaseConfig, TGBot) for required variables.

Security:
    - Keep .env files out of version control
    - Prefer environment variables for production secrets
"""

from dataclasses import dataclass
from typing import Type

from environs import Env


@dataclass
class DatabaseConfig:
    """Configuration for database connections

    Attributes:
        db_name (str): Database name
        db_host (str): Database host (localhost for example or IP-address)
        db_user (str): User's database name
        db_password (str): User's database name
        db_url (str): Postgres url
    """

    db_name: str
    db_host: str
    db_user: str
    db_password: str
    db_url: str


@dataclass
class TGBot:
    """Telegram bot configuration.

    Attributes:
        bot_token (str): bot token from @BotFather
        admin_ids (list[int]): list of bot's admins
    """

    bot_token: str
    admin_ids: list[int]


@dataclass
class Config:
    """Root app configuration

    Attributes:
        database_config (DatabaseConfig): Database config
        tg_bot (TGBot): TG Bot config
    """

    database_config: DatabaseConfig
    tg_bot: TGBot


def load_config(path: None | str = None) -> Config:
    """Load configuration from .env.

    Args:
        path: path to .env (if path is None, function will load from project root).

    Returns:
        Config: object of Config with bot and DB configuration.
    """
    env = Env()
    env.read_env(path)

    return Config(
        database_config=DatabaseConfig(
            db_name=env("DB_NAME"),
            db_host=env("DB_HOST"),
            db_user=env("DB_USER"),
            db_password=env("DB_PASSWORD"),
            db_url=env("DB_URL"),
        ),
        tg_bot=TGBot(
            bot_token=env("BOT_TOKEN"),
            admin_ids=list(map(int, env("ADMIN_IDS").split())),
        ),
    )
