
import os
import subprocess
from get_answers import Fetcher

class Commander:
    def __init__(self):
        self.confirm = [
            'yes', 'affirmative', 'si',
            'sure', 'do it', 'yeah', 'confirm']
        self.cancel = [
            'no', 'negative', 'negative soldier',
            'don\'t', 'wait', 'cancel']

    def discover(self, text):
        if 'what' in text and 'your name' in text:
            if 'my' in text:
                self.response(
                    'You haven\'t told me your name, yet.')
            else:
                self.respond(
                    'My name is python commander. How are you?')

        elif 'launch' in text or 'open' in text:
            app = text.split(' ', 1)[-1]
            self.response('Opening ' + app)
            os.system('open -a ' + app + '.app')

        else:
            f = Fetcher("https://www.google.com/search?q=" + text)
            a = f.lookup()
            self.respond(a)

    def respond(self, response):
        subprocess.call('say ' + response, shell=True)