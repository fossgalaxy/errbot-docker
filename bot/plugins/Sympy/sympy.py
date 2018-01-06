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

from sympy import sympify, SympifyError

from errbot import BotPlugin, botcmd


class Sympy(BotPlugin):
    """Use sympy for symbolic mathematics"""

    @botcmd
    def calc(self, message, args):
        """Calculates the simplifed form of a mathmatical expression"""
        if not args:
            return "**Usage**: !calc <expression>"

        try:
            e = sympify(args)
            return "```{} = {}```".format(args, + e)
        except SympifyError as err:
            return "**Error**: {}".format(err)
