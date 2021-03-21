from contextlib import suppress

from aiogram import Dispatcher
from aiogram.utils.exceptions import TelegramAPIError
from aiogram.utils.executor import Executor
from app import config
from app.misc import dp
from loguru import logger

runner = Executor(dp)


async def on_startup_notify(dispatcher: Dispatcher):
    with suppress(TelegramAPIError):
        await dispatcher.bot.send_message(
            chat_id=config.admin_id,
            text="Bot started!",
            disable_notification=True,
        )
        logger.info(
            f"Administrator {config.admin_id} notified about bot launch"
        )


def setup():
    logger.info("Configure executor...")
    runner.on_startup(on_startup_notify)
