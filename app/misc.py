from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from app import config
from loguru import logger

bot = Bot(config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot, storage=MemoryStorage())


def setup():
    from app import middlewares
    from app.utils import executor

    middlewares.setup(dp)
    executor.setup()

    logger.info("Configure handlers...")
    import app.handlers
