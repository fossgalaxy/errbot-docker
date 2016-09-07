from sympy import sympify

from errbot import BotPlugin, botcmd


class Sympy(BotPlugin):
    """Use sympy for symbolic mathematics"""

    @botcmd
    def calc(self, message, args):
        e = sympify(args)
        return "```{} = {}```".format(args, + e)
