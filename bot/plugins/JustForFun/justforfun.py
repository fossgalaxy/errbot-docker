from errbot import BotPlugin


class Justforfun(BotPlugin):
    """This is just for fun"""

    def callback_mention(self, message, mentioned_people):
        """ Listens for rude or nice things about the bot """
        if self.bot_identifier not in mentioned_people:
            return

        # The bot has been mentioned
        cmp_message = message.body.casefold()
        if 'thank' in cmp_message:
            self.send(message.to, "you're welcome")
        if 'silly' or 'bad' in cmp_message:
            self.send(message.to, "sorry")
