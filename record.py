class Record:
    def __init__(self):
        '''all flipping information for a legal move'''
        self.record = {"u": 0,
                       "d": 0,
                       "l": 0,
                       "r": 0,
                       "ul": 0,
                       "ur": 0,
                       "dl": 0,
                       "dr": 0
                       }

    def update(self, direction, steps):
        '''update flipping information'''
        assert direction in self.record, "Wrong Direction!!"
        self.record[direction] = steps
