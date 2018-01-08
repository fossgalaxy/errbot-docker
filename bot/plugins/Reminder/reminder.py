# Copyright © 2018 Bruce Cowan <bruce@bcowan.eu>
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
from threading import Timer

from dateparser import parse
from errbot import BotPlugin, botcmd

class ReminderType:
    def __init__(self, message, time, text):
        self.message = message
        self.time = time
        self.text = text

class Reminder(BotPlugin):
    """Allows reminder functionality"""

    def activate(self):
        super().activate()
        self.reminders = []

    @staticmethod
    def _separate_args(args):
        i = args.index(':')

        time_str = ' '.join(args[:i])
        time = parse(time_str, settings={'DATE_ORDER': 'DMY'})
        msg = ' '.join(args[i+1:])

        return time, msg

    def _timer_func(self, message, reminder):
        self.send(message.to, reminder.text, message)
        del self.reminders[self.reminders.index(reminder)]

    @staticmethod
    def _get_delta(time):
        now = datetime.now()
        if time < now:
            return "**Error**: Bot cannot time travel (yet)"

        return (time - now).seconds + 1

    @botcmd(split_args_with=None)
    def reminder_add(self, message, args):
        """ Add a reminder"""
        if len(args) < 2 or ':' not in args:
            return "**Usage**: !reminder add <time> : <message>"

        time, text = self._separate_args(args)
        if time is None:
            return "**Error**: Could not parse time"

        delta = self._get_delta(time)

        reminder = ReminderType(message, time, text)
        reminder.timer = Timer(delta, self._timer_func, [message, reminder])
        reminder.timer.start()

        self.reminders.append(reminder)

        return "Set timer for {}".format(time.strftime('%x %X'))

    @botcmd
    def reminder_list(self, message, args):
        """ List reminders"""
        reminders = list(enumerate(self.reminders))
        reminders = [(e[0], e[1].time.strftime('%x %X')) for e in reminders]
        for e in reminders:
            yield "{}: {}".format(e[0], e[1])

    @botcmd(split_args_with=None)
    def reminder_edit(self, message, args):
        """ Edit the message and time of a timer"""
        if len(args) < 3 or ':' not in args:
            return "**Usage**: !reminder edit <id> <time> : <message>"

        try:
            idx = int(args[0])
            edit = self.reminders[idx]
        except IndexError:
            return "**Error**: reminder '{}' not in database".format(args)
        else:
            time, text = self._separate_args(args[1:])
            if time is None:
                return "**Error**: Could not parse time"

            edit.message = text

            delta = self._get_delta(time)
            edit.timer.cancel()
            edit.timer = Timer(delta, self._timer_func, [message, edit])
            edit.timer.start()
            edit.time = time

            return "Edited reminder '{}'".format(args[0])

    @botcmd
    def reminder_remove(self, message, args):
        """ Remove the timer """
        if not args:
            return "**Usage**: !reminder remove <id>"

        try:
            idx = int(args)
            self.reminders[idx].timer.cancel()
            del self.reminders[idx]
            return "Deleted reminder '{}'".format(args)
        except IndexError:
            return "**Error**: reminder '{}' not in database".format(args)
