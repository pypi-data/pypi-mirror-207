class SolverStatus:

    def __init__(self):
        self.cycle = 0
        self.iiter = 0
        self.time = 0.0
        self.time0 = 0.0
        self.dtime = 0.0
        self.lam = 1.0

    def increase_step(self):
        self.cycle += 1
        self.time += self.dtime
        self.iiter = 0
