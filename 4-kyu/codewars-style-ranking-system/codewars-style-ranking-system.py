# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method
class User:
    def __init__(self):
        self.rank = -8
        self.progress = 0
    
    def inc_progress(self, task):
        if task < -8 or task > 8 or task == 0:
            raise error
        difference = task - self.rank
        if self.rank < 0 and task > 0:
            difference -= 1
        if self.rank == task:
            self.progress += 3
        elif self.rank - 1 == task or (self.rank == 1 and self.rank - 2 == task):
            self.progress += 1
        elif self.rank < task:
            self.progress += (10 * difference * difference)
        
        while self.progress >= 100:
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:
                self.rank += 1
        if self.rank >= 8:
            self.rank = 8
            self.progress = 0
            
#increment by 1 5 times increment by 2 2 times increment by -1