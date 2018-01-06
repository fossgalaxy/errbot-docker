# Copyright © 2016 Bruce Cowan <bruce@bcowan.eu>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

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

        yield ', '.join(sorted(self.factoids))

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
