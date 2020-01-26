from politricker import chainbase

class fakerooHandler(object):
    '''
    The fakeroo bot is a special implementation of the poliTricker API
    to get updated via a Zulip bot which can also take input for analysis
    '''

    def usage(self):
        return '''
        This bot provides users with an easy access chat
        to understand the current political scenario
        '''

    def handle_message(self, message, bot_handler):
        contents = message.to_lower().split()
        if contents[0] == "hello":
            return "Hi, use `@fakeroo help` to check the see what all you can do."
        elif contents[0] == "@fakeroo":
            results = chainbase.contract_address
            return "The results are in!\n%s" % results


handler_class = fakerooHandler