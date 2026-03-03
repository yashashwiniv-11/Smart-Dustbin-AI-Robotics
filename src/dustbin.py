class Dustbin:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.current_weight = 0

    def add_waste(self, weight):
        self.current_weight += weight

    def is_full(self):
        return self.current_weight >= self.capacity

    def status(self):
        if self.is_full():
            return "FULL"
        return "NOT FULL"# Force update commit
# Force update commit
# Confirm file is tracked
