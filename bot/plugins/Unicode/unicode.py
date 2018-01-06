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
