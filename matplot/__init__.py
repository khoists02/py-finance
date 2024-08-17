import matplotlib.pyplot as plt


class Matplot:
    instance = None
    FONTDICS = {'fontname': 'Comic Sans MS', 'fontsize': 16, 'color': '#d1d1d1', 'fontweight': 'bold'}

    def __init__(self, x, y, plots):
        self.x = x
        self.y = y
        self.plots = plots

    def draw(self):
        types = ['b.-', 'r.-', 'g.-']  # type plot chart
        plt.title('TESTING', fontdict=self.FONTDICS)  # title and font config
        for idx, dt in enumerate(self.plots):
            plt.plot(self.x, self.y[idx], types[idx], label=dt)  # plot data

        # TODO: how to shoe legends.
        plt.xlabel('Time')
        plt.ylabel('Dolar')
        # show label with label in plot
        plt.legend()
        # show chart
        plt.show()
