import pgzero.clock

class Animation:

    def __init__(self, actors, pos, period, speed_x=0, speed_y=0, repeat=False):
        self.actors = actors
        self.pos = pos
        self.clock = pgzero.clock
        self.period = period
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.repeat = False
        self._idx = 0        
        
    def draw(self):
        if self.running():
            self.actors[self._idx].pos = self.pos
            self.actors[self._idx].draw()
            
    def update(self):
        pass
            
    def next(self):
        if self.running():
            self.pos = (self.pos[0]+self.speed_x, self.pos[1]+self.speed_y)
            self._idx += 1
            if self._idx  >= len(self.actors):
                if self.repeat:
                    self.idx = 0
            self.clock.schedule(self.next, self.period)

    def start(self):
        self.clock.schedule(self.next, self.period)

    def running(self):
        return self._idx < len(self.actors)
    
    def stopped(self):
        return not self.running()
