from random import choice

from errbot import BotPlugin, botcmd


class Factoid(BotPlugin):
    """A store of strings of text"""

    def activate(self):
        super().activate()
        try:
            self.factoids = self['factoids']
        except KeyError:
            self.factoids = {}

    def deactivate(self):
        self['factoids'] = self.factoids
        super().deactivate()

    @botcmd(split_args_with=None)
    def factoid_add(self, message, args):
        if not args:
            return "**Usage**: !factoid add <name> <text>"
        if len(args) < 2:
            return "**Error**: Not enough arguments given"

        name = args[0]
        text = ' '.join(args[1:])
        self.factoids[name] = text
        return "Added factoid '{}': '{}'".format(name, text)

    @botcmd
    def factoid_get(self, message, args):
        if not args:
            return "**Usage**: !factoid get <name>"

        try:
            return self.factoids    [args]
        except KeyError:
            return "**Error**: factoid '{}' not in database".format(args)

    @botcmd
    def factoid_list(self, message, args):
        """Gets a list of the factoids in the database"""
        for n, v in self.factoids.items():
            yield "{}: {}".format(n, v)

    @botcmd
    def factoid_random(self, message, args):
        rand = choice(list(self.factoids.items()))
        return "{}: {}".format(rand[0], rand[1])

    @botcmd
    def factoid_remove(self, message, args):
        if not args:
            return "**Usage**: !factoid remove <name>"

        try:
            del self.factoids[args]
            return "Deleted {} factoid".format(args)
        except KeyError:
            return "**Error**: factoid '{}' not in database".format(args)