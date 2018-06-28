class FrameCounter:
    def __init__(self, count_max):
        self.count = 0
        self.count_max = count_max
        self.expired = False

    def run(self):
        if self.count < self.count_max:
            self.count += 1
        else:
            self.expired = True

    def reset(self):
        self.count = 0
        self.expired = False

