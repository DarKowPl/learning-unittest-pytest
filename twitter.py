import re


class Twitter:
    version = '1.0'

    def __init__(self):
        self.tweets = []

    def tweet(self, message):
        if len(message) > 160:
            raise Exception('The message is too long')
        self.tweets.append(message)

    def find_hashtags(self, message):
        return [m.lower() for m in re.findall(r'#(\w+)', message)]

    def delete(self):
        print("It's the end")
