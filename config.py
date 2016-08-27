import json

class Config:
    def __init__(self):
        with open('config.json') as json_file:
            data = json.load(json_file)
            self.server = data['server']
            self.port = data['port']
            self.nick = data['nick']
            self.realname = data['realname']
            self.channels = data['channels']
