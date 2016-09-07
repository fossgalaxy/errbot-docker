from sympy import sympify

from errbot import BotPlugin, botcmd


class Sympy(BotPlugin):
    """Use sympy for symbolic mathematics"""

    @botcmd
    def calc(self, message, args):
        """Calculates the simplifed form of a mathmatical expression"""
        if not args:
            return "**Usage**: !calc <expression>"

        e = sympify(args)
        return "```{} = {}```".format(args, + e)
