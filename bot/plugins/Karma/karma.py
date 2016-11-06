from collections import defaultdict

from errbot import BotPlugin, botcmd


class Karma(BotPlugin):
    """Karma service"""

    def activate(self):
        super().activate()

        self.karma = self.get('karma', defaultdict(int))

    def deactivate(self):
        self['karma'] = self.karma

        super().deactivate()

    @botcmd
    def karma_list(self, message, args):
        """Prints a list of karmaed things"""
        if self.karma:
            l = ', '.join(self.karma.keys())
            return "List: '{}'".format(l)
        else:
            return "**Warning**: Nothing in the karma database"

    @botcmd
    def karma_add(self, message, args):
        """Adds karma"""
        if not args:
            return "**Usage**: !karma add <target>"

        self.karma[args] += 1
        return "Karma for '{}' is now {}".format(args, self.karma[args])

    @botcmd
    def karma_remove(self, message, args):
        """Removes karma"""
        if not args:
            return "**Usage**: !karma remove <target>"

        self.karma[args] -= 1
        return "Karma for '{}' is now {}".format(args, self.karma[args])

    @botcmd
    def karma(self, message, args):
        """Gets karma"""
        if not args:
            return "**Usage**: !karma <target>"

        return "Karma for '{}' is {}".format(args, self.karma[args])
