import logging
import os

# Core config

BACKEND = 'Matrix'  # defaults to XMPP
STORAGE = 'Shelf'  # defaults to filestorage (python shelf).

##
# File Paths
##

# data directories
BASE_DIR = os.getenv('BOT_BASE_DIR', os.getcwd() )
BOT_DATA_DIR = os.getenv('BOT_DATA_DIR', os.path.join(BASE_DIR, 'data') )

# Extra search paths
# defaults: ./code/plugins and ./code/backends
EXTRA_DIR = os.getenv('BOT_EXTRA_DIR', os.path.join(BASE_DIR, 'extra') )
BOT_EXTRA_PLUGIN_DIR = os.getenv('BOT_PLUGIN_DIR', os.path.join(EXTRA_DIR, 'plugins'))
BOT_EXTRA_BACKEND_DIR = os.getenv('BOT_BACKEND_DIR', os.path.join(EXTRA_DIR, 'backends'))
BOT_EXTRA_STORAGE_PLUGINS_DIR = os.getenv('BOT_STORAGE_DIR', os.path.join(EXTRA_DIR, 'storage'))

# Plugin config
PLUGINS_CALLBACK_ORDER = (None, )

# Logging config

BOT_LOG_FILE = BOT_DATA_DIR + '/err.log'
BOT_LOG_LEVEL = logging.INFO

BOT_LOG_SENTRY = False

# Account config

BOT_IDENTITY = {
    'homserver': os.getenv('BOT_SERVER', 'https://matrix.fgmx.uk'),
    'username': os.getenv('BOT_USER', '@errbot:fossgalaxy.com'),
    'password': os.getenv('BOT_PASSWORD', None),
    'device': os.getenv('BOT_DEVICE', 'errbot'),
    'device_id': os.getenv('BOT_DEVICE_ID', None),
    'token': os.getenv('BOT_TOKEN', None)
}

# admins to be set via BOT_ADMINS environment variable (default to anyone connected though moggy)
BOT_ADMINS = os.getenv("BOT_ADMINS", "@webpigeon:fossgalaxy.com").split(",")
#CHATROOM_PRESENCE = ('#fossgalaxy',)

# QOL improvements
BOT_PREFIX_OPTIONAL_ON_CHAT = True
BOT_ALT_PREFIXES = ('Err',)

# Avoid spam
DIVERT_TO_PRIVATE = ()
DIVERT_TO_THREAD = ()

CHATROOM_RELAY = {}
REVERSE_CHATROOM_RELAY = {}

# Command cleanup
COMPACT_OUTPUT = False
SUPPRESS_CMD_NOT_FOUND = True
