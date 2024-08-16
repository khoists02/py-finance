import matplotlib.pyplot as plt

class Matplot:
    instance = None
    def __init__(self,  x, y, plots):
        self.x = x
        self.y = y
        self.plots = plots

    def draw(self):
        lines = []
        for idx, dt in enumerate(self.plots):
            lines.append(plt.plot(self.x, self.y[idx]))
        # TODO: how to shoe legends.
        # plt.legend(lines, self.plots)
        plt.show()



