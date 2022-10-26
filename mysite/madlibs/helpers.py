class myRange:

    def restartFrom(self, start):
        self.start = start

    def get(self, start, end):
        self.start = start
        while self.start != end:
            yield self.start
            self.start += 1
