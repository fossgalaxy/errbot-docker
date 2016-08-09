#!/usr/bin/env python3

import irc.bot

class FossGalaxyBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, 'UC Botty McBotface')
        self.channel = channel

        self.lines = []

    def on_nicknameinuse(self, conn, event):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, conn, event):
        c.join(self.channel)

    def on_pubmsg(self, conn, event):
        if 'uc_pybot' not in event.source:
            self.lines.append(event.arguments)

        text = '{} lines spoken'.format(len(self.lines))
        conn.privmsg(self.channel, text)

if __name__ == '__main__':
    bot = FossGalaxyBot('#fossgalaxy', 'uc_pybot', 'irc.freenode.net')
    bot.start()
