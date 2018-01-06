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
