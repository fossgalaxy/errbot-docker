from random import choice

from errbot import BotPlugin, botcmd


class Lart(BotPlugin):
    """Issue larts to people"""

    def activate(self):
        super().activate()
        
        try:
            self.larts = self['larts']
        except KeyError:
            self.larts = []

    def deactivate(self):
        self['larts'] = self.larts
        super().deactivate()

    @botcmd
    def lart(self, message, args):
        """Insult a target"""
        try:
            lart = choice(self.larts)
            return lart.format(args)
        except IndexError:
            return "**Error**: There are no larts in the database"

    @botcmd
    def lart_add(self, message, args):
        """Add a lart, requires a part '{}' which will be replaced with target"""
        if '{}' not in args:
           return "**Error**: '{}' not in message"

        self.larts.append(args)
        return "Added '{}' to the database".format(args)

    @botcmd
    def lart_list(self, message, args):
        """Gets a list of the larts in the database"""
        for i, l in enumerate(self.larts):
            yield "{}: {}".format(i, l)

    @botcmd
    def lart_get(self, message, args):
        """Gets the format string of a specific lart"""
        try:
            return "{}".format(self.larts[int(args)])
        except (IndexError, ValueError) as e:
            return "**Error**: {}".format(e)

    @botcmd
    def lart_remove(self, message, args):
        """Remove a lart from the database"""
        try:
            del self.larts[int(args)]
            return "Lart {} removed".format(int(args))
        except (IndexError, ValueError) as e:
            return "**Error**: {}".format(e)
