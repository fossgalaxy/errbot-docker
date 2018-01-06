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

from datetime import datetime

from errbot import BotPlugin, botcmd


class Datetime(BotPlugin):
    """Functions to do with dates and times"""

    @staticmethod
    def _get_date_time(fmt):
        dt = datetime.now()
        return dt.strftime(fmt)

    @botcmd
    def date(self, message, args):
        """Displays the current date in the current locale"""
        return "The date is " + self._get_date_time('%x')

    @botcmd
    def time(self, message, args):
        """Displays the current time in the current locale"""
        return "The time is " + self._get_date_time('%X')

    @botcmd
    def strftime(self, message, args):
        """Formatted date and/or time using strftime"""
        if not args:
            return "**Usage**: !datetime strftime <format>"
        return "The date and time is " + self._get_date_time(args)
