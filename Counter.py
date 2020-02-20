class Counters:
    def __init__(self, n):
        self.row_size = n + 1
        self.col_size = n * 10
        self.start_space = n
        self.middle_top_space = n
        self.middle_bottom_space = 1
        self.middle_decrease_stars = 1
        self.stars = n

    def increase(self):
        self.start_space -= 1
        self.middle_top_space -= 2
        self.stars += 2

    def decrease(self):
        self.start_space -= 1
        self.middle_bottom_space += 2
        self.middle_decrease_stars += 2
