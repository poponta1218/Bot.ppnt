import os
from os.path import join, dirname
from dotenv import load_dotenv

load_dotenv(verbose=True)

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")