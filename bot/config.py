import logging
import os

# Core config

BACKEND = 'IRC'  # defaults to XMPP
STORAGE = 'Shelf'  # defaults to filestorage (python shelf).
BOT_DATA_DIR = './log'

# Plugin config

BOT_EXTRA_PLUGIN_DIR = 'plugins'
PLUGINS_CALLBACK_ORDER = (None, )

# Logging config

BOT_LOG_FILE = BOT_DATA_DIR + '/err.log'
BOT_LOG_LEVEL = logging.INFO
BOT_LOG_SENTRY = False
SENTRY_DSN = ''
SENTRY_LOGLEVEL = BOT_LOG_LEVEL

# Account config

BOT_IDENTITY = {
    'nickname' : 'uc_errbot',
    # 'username' : 'err-chatbot',    # optional, defaults to nickname if omitted
    # 'password' : None,             # optional
    'server' : 'irc.freenode.net',
    'port': 6697,                  # optional
    'ssl': True,                  # optional
    # 'ipv6': False,                 # optional
    # 'nickserv_password': None,     # optional
    ## Optional: Specify an IP address or hostname (vhost), and a
    ## port, to use when making the connection. Leave port at 0
    ## if you have no source port preference.
    ##    example: 'bind_address': ('my-errbot.io', 0)
    # 'bind_address': ('localhost', 0),
}

# admins to be set via BOT_ADMINS environment variable (default to anyone connected though kat)
BOT_ADMINS = os.getenv("BOT_ADMINS", "*!*@kat.vps.livebytes.co.uk").split(",")
CHATROOM_PRESENCE = ('#fossgalaxy', "#unity-coders")
DIVERT_TO_PRIVATE = ()
CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}
