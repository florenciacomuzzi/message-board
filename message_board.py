#!/usr/bin/python3
import sys
import uuid


class MessageBoard(object):

    messages = {}
    messages["abcde"] =  'My first message'

    def get_messages(self):
        return self.messages

    def post_message(self, user, msg):
        if user == "":
            user = "anon"
        self.messages[user] = msg

    def get_message_by_id(self, id):
        pass

    def get_unique_id(self):
        return str(uuid.uuid4())[:8]

    def get_message(self, key):
        return self.messages[key]

if __name__ == '__main__':
    message_board = MessageBoard()

    print('Welcome to MessageBoard!')
    print('Enter \"list\" to see all messages.')
    print('Enter \"post\" to post a message.')
    print('Enter \"exit\" to destroy me.')
    print('Enter \"message\" to find me.\n')
    while True:
        cmd = input('Your wish is my command > ')
        if cmd == 'list':
            print(message_board.get_messages())
        elif cmd == 'post':
            usermsg = input('Username > ')
            msg = input('Message > ')
            message_board.post_message(usermsg, msg)
        elif cmd == 'message':
            key = input('Key > ')
            message = message_board.get_message(key)
            print(message)
        elif cmd == 'exit':
            sys.exit()
