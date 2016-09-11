from random import choice

from errbot import BotPlugin, botcmd


class Factoid(BotPlugin):
    """A store of strings of text"""

    def activate(self):
        super().activate()

        self.factoids = self.get('factoids', {})

    def deactivate(self):
        self['factoids'] = self.factoids

        super().deactivate()

    @botcmd
    def factoid(self, message, args):
        """Get a factoid from the database"""
        if not args:
            return "**Usage**: !factoid get <name>"

        try:
            return self.factoids[args]
        except KeyError:
            return "**Error**: factoid '{}' not in database".format(args)

    @botcmd(split_args_with=None)
    def factoid_add(self, message, args):
        """Add a factoid to the database"""
        if len(args) < 2:
            return "**Usage**: !factoid add <name> <text>"

        name = args[0]
        text = ' '.join(args[1:])
        self.factoids[name] = text
        return "Added factoid '{}': '{}'".format(name, text)

    @botcmd
    def factoid_list(self, message, args):
        """Gets a list of the factoids in the database"""
        if not self.factoids:
            yield "There are no factoids"

        for name in sorted(self.factoids.keys()):
            yield name

    @botcmd
    def factoid_random(self, message, args):
        """Get a random factoid from the database"""
        if not self.factoids:
            return "There are no factoids"

        rand = choice(list(self.factoids.items()))
        return "{}: {}".format(rand[0], rand[1])

    @botcmd
    def factoid_remove(self, message, args):
        """Remove a factoid from the database"""
        if not args:
            return "**Usage**: !factoid remove <name>"

        try:
            del self.factoids[args]
            return "Deleted factoid '{}'".format(args)
        except KeyError:
            return "**Error**: factoid '{}' not in database".format(args)
