import argparse
import sys


class MessageBoard(object):

    messages = ['My first message']

    def get_messages(self):
        return self.messages

    def post_message(self, msg):
        self.messages.append(msg)

    def get_message_by_id(self, id):
        pass


if __name__ == '__main__':
    message_board = MessageBoard()

    print('Welcome to MessageBoard!')
    print('Enter \"list\" to see all messages.')
    print('Enter \"post\" to post a message.')
    print('Enter \"exit\" to destroy me.\n')
    while True:
        cmd = input('Your wish is my command > ')
        if cmd == 'list':
            print(message_board.get_messages())
        elif cmd == 'post':
            msg = input('Message > ')
            message_board.post_message(msg)
        elif cmd == 'exit':
            sys.exit()
