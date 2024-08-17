import matplotlib.pyplot as plt

class Matplot:
    instance = None
    def __init__(self,  x, y, plots):
        self.x = x
        self.y = y
        self.plots = plots

    def draw(self):
        types = ['b.-', 'r.-', 'g.-']
        for idx, dt in enumerate(self.plots):
            plt.plot(self.x, self.y[idx], types[idx], label=dt)

        # TODO: how to shoe legends.
        plt.xlabel('Time')
        plt.ylabel('Dolar')
        plt.legend()
        plt.show()



