#!/usr/bin/env python3

import irc.bot

class FossGalaxyBot(irc.bot.SingleServerIRCBot):
    def __init__(self, channel, nickname, server, port=6667):
        irc.bot.SingleServerIRCBot.__init__(self, [(server, port)], nickname, 'UC Botty McBotface')
        self.channel = channel

        self.lines = []

    def on_nicknameinuse(self, c, e):
        c.nick(c.get_nickname() + "_")

    def on_welcome(self, c, e):
        c.join(self.channel)

    def on_pubmsg(self, c, e):
        if 'uc_pybot' not in e.source:
            self.lines.append(e.arguments)
        
        text = '{} lines spoken'.format(len(self.lines))
        c.privmsg('#fossgalaxy', text)

if __name__ == '__main__':
    bot = FossGalaxyBot('#fossgalaxy', 'uc_pybot', 'irc.freenode.net')
    bot.start()
