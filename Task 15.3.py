class TVController:
    def __init__(self, channels):
        self.channels = channels
        self.current_channel_index = 0

    def first_channel(self):
        self.current_channel_index = 0
        return self.current_channel()

    def last_channel(self):
        self.current_channel_index = len(self.channels) - 1
        return self.current_channel()

    def turn_channel(self, n):
        if 1 <= n <= len(self.channels):
            self.current_channel_index = n - 1
        return self.current_channel()

    def next_channel(self):
        self.current_channel_index = (self.current_channel_index + 1) % len(self.channels)
        return self.current_channel()

    def previous_channel(self):
        self.current_channel_index = (self.current_channel_index - 1) % len(self.channels)
        return self.current_channel()

    def current_channel(self):
        return self.channels[self.current_channel_index]

    def is_exist(self, n_or_name):
        if isinstance(n_or_name, int):
            return "Yes" if 1 <= n_or_name <= len(self.channels) else "No"
        elif isinstance(n_or_name, str):
            return "Yes" if n_or_name in self.channels else "No"


CHANNELS = ["BBC", "Discovery", "TV1000"]
controller = TVController(CHANNELS)

print(controller.first_channel())  # "BBC"
print(controller.last_channel())  # "TV1000"
print(controller.turn_channel(1))  # "BBC"
print(controller.next_channel())  # "Discovery"
print(controller.previous_channel())  # "BBC"
print(controller.current_channel())  # "BBC"
print(controller.is_exist(4))  # "No"
print(controller.is_exist("BBC"))  # "Yes"
