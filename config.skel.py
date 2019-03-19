import logging
import os

# Core config

BACKEND = 'IRC'  # defaults to XMPP
STORAGE = 'Shelf'  # defaults to filestorage (python shelf).
BOT_DATA_DIR = '/home/errbot/bot/data'

# Plugin config

BOT_EXTRA_PLUGIN_DIR = 'plugins'
PLUGINS_CALLBACK_ORDER = (None, )

# Logging config

BOT_LOG_FILE = BOT_DATA_DIR + '/err.log'
BOT_LOG_LEVEL = logging.INFO
BOT_LOG_SENTRY = os.getenv('BOT_SENTRY_ENABLE', 'no') == 'yes'
SENTRY_DSN = os.getenv('BOT_SENTRY_DSN', '')
SENTRY_LOGLEVEL = BOT_LOG_LEVEL

# Account config

BOT_IDENTITY = {
    'nickname' : os.getenv("IRC_NICK", "uc_errbot"),
    # 'username' : 'err-chatbot',    # optional, defaults to nickname if omitted
    # 'password' : None,             # optional
    'server' : os.getenv('IRC_HOST', 'irc.freenode.net'),
    'port': int(os.getenv('IRC_PORT', '6697')),                  # optional
    'ssl': True,                  # optional
    # 'ipv6': False,                 # optional
    'nickserv_password': os.getenv("NICKSERV_PASSWORD", None),     # optional
    ## Optional: Specify an IP address or hostname (vhost), and a
    ## port, to use when making the connection. Leave port at 0
    ## if you have no source port preference.
    ##    example: 'bind_address': ('my-errbot.io', 0)
    # 'bind_address': ('localhost', 0),
}

# admins to be set via BOT_ADMINS environment variable (default to anyone connected though moggy)
BOT_ADMINS = os.getenv("BOT_ADMINS", "*!*@moggy.vps.webpigeon.me.uk").split(",")
CHATROOM_PRESENCE = ('#fossgalaxy',)
DIVERT_TO_PRIVATE = ()
CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}
