import os

from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = str(os.getenv("BOT_TOKEN"))
admin_id = str(os.getenv("admin_id"))
