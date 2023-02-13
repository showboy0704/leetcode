class MyCalendarTwo:
    def __init__(self):
        self.events = []
        self.doubles = []

    def book(self, start, end):
        for i, j in self.doubles:
            if start < j and end > i:
                return False
        for i, j in self.events:
            if start < j and end > i:
                self.doubles.append((max(start, i), min(end, j)))
        self.events.append((start, end))
        return True