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

from errbot import BotPlugin


class Justforfun(BotPlugin):
    """This is just for fun"""

    def callback_mention(self, message, mentioned_people):
        """ Listens for rude or nice things about the bot """
        if self.bot_identifier not in mentioned_people:
            return

        # The bot has been mentioned
        cmp_message = message.body.casefold()

        good = ['thank']
        bad = ['silly', 'bad']
        congrat = ['congrats', 'congratulations']

        if any(s in cmp_message for s in good):
            self.send(message.to, "you're welcome", message)
        if any(s in cmp_message for s in bad):
            self.send(message.to, "sorry", message)
        if any(s in cmp_message for s in congrat):
            self.send(message.to, "thank you", message)
