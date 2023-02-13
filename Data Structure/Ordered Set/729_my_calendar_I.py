class MyCalendar:

    def __init__(self):
        self.events = [[-2, -1], [float('inf')]]

    def book(self, start: int, end: int) -> bool:
        for i in range(len(self.events)-1):
            if self.events[i][1] <= start and end <= self.events[i+1][0]:
                self.events.insert(i+1, [start, end])
                return True
        return False
