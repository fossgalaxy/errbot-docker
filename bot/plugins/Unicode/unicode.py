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
        except ValueError as e:
            return "Error: {}".format(e)
