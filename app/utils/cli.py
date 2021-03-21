"""
Шаблон этого файла был взят из github.com/bomzheg/KarmaBot/blob/master/app/utils/cli.py
Были убраны все функции и переменные касающиеся вэб-хуков, т.к. их я не использую
"""
import argparse
import functools

from app import config
from loguru import logger


def create_parser():
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument(
        "-s",
        "--skip-updates",
        action="store_const",
        const=True,
        help="Skip pending updates",
    )
    return arg_parser


def cli():
    def polling(skip_updates: bool):
        """
        Запуск бота на лонгпуллинге
        """
        from app.utils.executor import runner

        logger.info("Starting polling...")

        runner.skip_updates = skip_updates
        runner.start_polling()

    parser = create_parser()
    namespace = parser.parse_args()

    from app import misc

    misc.setup()
    if namespace.skip_updates:
        polling(namespace.skip_updates)
