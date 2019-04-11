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
    print(message_board.get_messages())
