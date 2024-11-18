from game_config.messages import EVENT_MESSAGES

class Map:
    def __init__(self, size):
        self.size = size
        self.messages = EVENT_MESSAGES

    def get_message(self, position):
        return self.messages[position % len(self.messages)]
