# Copyright (c) 2025 devgagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

import os
from dotenv import load_dotenv

load_dotenv()

# Pehle environment variables read karein
API_ID = int(os.getenv("API_ID", ""))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, os.getenv("OWNER_ID", "").split()))
MONGO_DB = os.getenv("MONGO_DB", "")
LOG_GROUP = os.getenv("LOG_GROUP", "")
CHANNEL_ID = int(os.getenv("CHANNEL_ID", ""))
FREEMIUM_LIMIT = int(os.getenv("FREEMIUM_LIMIT", "0"))
PREMIUM_LIMIT = int(os.getenv("PREMIUM_LIMIT", "0"))
WEBSITE_URL = os.getenv("WEBSITE_URL", "upshrink.com")
AD_API = os.getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = os.getenv("STRING", None)
DEFAULT_SESSION = os.getenv("DEFAUL_SESSION", None)  # added old method of invite link joining

# Phir default values define karein
INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# write here yt cookies
"""

# Ab in default values ko use kar sakte hain
YT_COOKIES = os.getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = os.getenv("INSTA_COOKIES", INST_COOKIES)
