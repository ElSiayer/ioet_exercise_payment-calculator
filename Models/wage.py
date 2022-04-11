class Wage:
    def __init__(self, start, end, rate):
        self.start = start
        self.end = end
        self.rate = rate
    
    def __str__(self):
        return f"{self.start}-{self.end}:{self.rate}"