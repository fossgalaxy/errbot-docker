from collections import defaultdict

from errbot import BotPlugin, botcmd


class Karma(BotPlugin):
    """Karma service"""

    def activate(self):
        super().activate()

        try:
            self.karma = self['karma']
        except KeyError:
            self.karma = self['karma'] = defaultdict(int)

    @botcmd
    def karma_add(self, message, args):
        """Adds karma"""
        self.karma[args] += 1
        return "Karma for {} is now {}".format(args, self.karma[args])

    @botcmd
    def karma_remove(self, message, args):
        """Removes karma"""
        self.karma[args] -= 1
        return "Karma for {} is now {}".format(args, self.karma[args])     

    @botcmd
    def karma(self, message, args):
        """Gets karma"""
        return "Karma for {} is {}".format(args, self.karma[args])
