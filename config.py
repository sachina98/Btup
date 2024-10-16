import os
class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7322375922:AAHTpAuGhBnC1CJyzaAqRRoOQ7K0_AfkzmY")
    
    API_ID = int(os.environ.get("API_ID", "28174664"))
    API_HASH = os.environ.get("API_HASH", "f504bf34ad7dbc597c8802db2f46453c")
    AUTH_USERS = os.environ.get("AUTH_USERS","5758937746")
    
