#!/usr/bin/env python3

from irc.bot import SingleServerIRCBot

from config import Config

class FossGalaxyBot(SingleServerIRCBot):
    def __init__(self, config):
        SingleServerIRCBot.__init__(self, [(config.server, config.port)],
                                    config.nick, config.realname)

        self._channels = config.channels
        self._lines = []

    def on_nicknameinuse(self, conn, event):
        conn.nick(c.get_nickname() + "_")

    def on_welcome(self, conn, event):
        for channel in self._channels:
            conn.join(channel)

    def on_pubmsg(self, conn, event):
        if 'uc_pybot' not in event.source:
            self._lines.append(event.arguments)

        text = '{} lines spoken'.format(len(self._lines))
        conn.privmsg(event.target, text)

if __name__ == '__main__':
    config = Config()
    bot = FossGalaxyBot(config)
    bot.start()
