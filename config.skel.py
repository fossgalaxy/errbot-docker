import logging
import os

# Core config

BACKEND = 'IRC'  # defaults to XMPP
STORAGE = 'Shelf'  # defaults to filestorage (python shelf).
BOT_DATA_DIR = '/home/errbot/bot/data'

# Plugin config

BOT_EXTRA_PLUGIN_DIR = None
PLUGINS_CALLBACK_ORDER = (None, )

# Logging config

BOT_LOG_FILE = BOT_DATA_DIR + '/err.log'
BOT_LOG_LEVEL = logging.INFO

BOT_LOG_SENTRY = False

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

# QOL improvements
BOT_PREFIX_OPTIONAL_ON_CHAT = True
OT_ALT_PREFIXES = ('Err',)

# Avoid spam
DIVERT_TO_PRIVATE = ()
DIVERT_TO_THREAD = ()

CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}

# IRC options
IRC_CHANNEL_RATE = 1  # Regular channel messages
IRC_PRIVATE_RATE = 1  # Private messages
IRC_RECONNECT_ON_KICK = 5  # Reconnect back to a channel after a kick (in seconds)
                            # Put it at None if you don't want the chat to
                            # reconnect
IRC_RECONNECT_ON_DISCONNECT = 5  # Reconnect back to a channel after a disconnection (in seconds)

COMPACT_OUTPUT = True

# play nice with civil
SUPPRESS_CMD_NOT_FOUND = True