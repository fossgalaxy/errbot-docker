from random import choice

from errbot import BotPlugin, botcmd


class Lart(BotPlugin):
    """Issue larts to people"""

    def activate(self):
        super().activate()
        
        self.larts = self.get('larts', [])

    def deactivate(self):
        self['larts'] = self.larts

        super().deactivate()

    @botcmd
    def lart(self, message, args):
        """Insult a target"""
        if not args:
            return "**Usage**: !lart <target>"

        try:
            lart = choice(self.larts)
            return lart.format(args)
        except IndexError:
            return "**Error**: There are no larts in the database"

    @botcmd
    def lart_add(self, message, args):
        """Add a lart, requires a part '{}' which will be replaced with target"""
        if not args:
            return "**Usage**: !lart add <pattern>"
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
        if not args:
            return "**Usage**: !lart get <id>"

        try:
            return "{}".format(self.larts[int(args)])
        except IndexError:
            return "**Error**: Lart {} not in database".format(args)
        except ValueError:
            return "**Error**: ID given couldn't be converted to an integer"

    @botcmd
    def lart_remove(self, message, args):
        """Remove a lart from the database"""
        if not args:
            return "**Usage**: !lart remove <id>"

        try:
            del self.larts[int(args)]
            return "Lart {} removed".format(int(args))
        except IndexError:
            return "**Error**: Lart {} not in database".format(args)
        except ValueError:
            return "**Error**: ID given couldn't be converted to an integer"

    @botcmd(split_args_with=None)
    def lart_edit(self, message, args):
        """Edit a lart in the database"""
        if len(args) < 2:
            return "**Usage**: !lart edit <id> <pattern>"
        if '{}' not in args:
            yield "**Error**: '{}' not in message"

        try:
            i = int(args[0])
            text = ' '.join(args[1:])
            self.larts[i] = text
            return "Changed lart {} to '{}'".format(i, text)
        except IndexError:
            yield "**Error**: Lart {} not in database".format(i)
        except ValueError:
            yield "**Error**: ID given couldn't be converted to an integer"
