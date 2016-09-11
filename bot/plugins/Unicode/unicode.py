import unicodedata

from errbot import BotPlugin, botcmd


class Unicode(BotPlugin):
    """Details about unicode characters"""

    @botcmd
    def ord(self, message, args):
        """Runs ord() on the characters given"""
        if not args:
            return "**Usage**: !ord <characters>"

        return [ord(c) for c in args]

    @botcmd
    def chr(self, message, args):
        """Runs chr() on the numbers given"""
        if not args:
            return "**Usage**: !chr <numbers>"

        try:
            return ''.join([chr(int(i)) for i in args.split()])
        except ValueError:
            return "**Error**: Needs integers"

    @botcmd
    def unicode_lookup(self, message, args):
        """Looks up a character by name"""
        if not args:
            return "**Usage**: !unicode lookup <name>"

        try:
            return "Character is {}".format(unicodedata.lookup(args))
        except KeyError:
            return "**Error**: Character not found"

    @botcmd
    def unicode_name(self, message, args):
        """Looks up the name of a character"""
        if len(args) != 1:
            return "**Usage**: !unicode name <chr>"

        try:
            return "Character's name is {}".format(unicodedata.name(args))
        except ValueError:
            return "**Error**: Character not found"
