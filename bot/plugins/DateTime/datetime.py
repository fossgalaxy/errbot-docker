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
        return "The date is " + self._get_date_time('%x')

    @botcmd
    def time(self, message, args):
        return "The time is " + self._get_date_time('%X')

    @botcmd
    def strftime(self, message, args):
        if not args:
            return "**Usage**: !datetime strftime <format>"
        return "The date and time is " + self._get_date_time(args)
