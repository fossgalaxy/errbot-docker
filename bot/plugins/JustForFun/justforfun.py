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
