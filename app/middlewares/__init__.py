from aiogram import Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from app.middlewares.throttling import ThrottlingMiddleware
from loguru import logger


def setup(dp: Dispatcher):
    logger.info("Configure middlewares...")
    dp.middleware.setup(ThrottlingMiddleware())
    dp.middleware.setup(LoggingMiddleware())
    logger.info("Middlewares are successfully configured")
