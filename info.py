import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
API_ID = int(environ['API_ID'])
API_HASH = environ['API_HASH']
BOT_TOKEN = environ['BOT_TOKEN']

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('AUTH_CHANNEL')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]

# MongoDB information
DATABASE_URI = environ['DATABASE_URI']
DATABASE_NAME = environ['DATABASE_NAME']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
 Hi This Official Bot For [📽 ᴄɪɴᴇᴍᴀ ᴄᴏᴍᴘᴀɴʏ 📽](https://t.me/CinemaCompany_Group)  [🟢ᴄɪɴᴇᴍᴀ ᴛᴀʟᴋɪᴇꜱ 🟢](https://t.me/Cinema_Talkies_Group) Groups Join This Group This For Use Bot
"""
START_MSG = environ.get('START_MSG', default_start_msg)

FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}({file_size}) 
▬▬▬▬▬▬▬▬▬▬▬▬▬▬
താഴെയുള്ള ലിങ്കിൽ ക്ലിക്ക് ചെയ്ത് ഗ്രൂപ്പിൽ ജോയിൻ ആയ ശേഷം സിനിമ ഡൌൺലോഡ് ചെയ്യുക. അല്ലെങ്കിൽ ഫയൽ വർക്ക്‌ ആവില്ല 😪
🚦Group 1👉  [📽 ᴄɪɴᴇᴍᴀ ᴄᴏᴍᴘᴀɴʏ 📽](https://t.me/CinemaCompany_Group) 
🚦Group 2👉 [🟢ᴄɪɴᴇᴍᴀ ᴛᴀʟᴋɪᴇꜱ 🟢](https://t.me/Cinema_Talkies_Group) ")
OMDB_API_KEY = environ.get("OMDB_API_KEY", "")
if FILE_CAPTION.strip() == "":
    CUSTOM_FILE_CAPTION=None
else:
    CUSTOM_FILE_CAPTION=FILE_CAPTION
if OMDB_API_KEY.strip() == "":
    API_KEY=None
else:
    API_KEY=OMDB_API_KEY
