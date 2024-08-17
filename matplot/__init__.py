import matplotlib.pyplot as plt

FONTDICS = {'fontname': 'Comic Sans MS', 'fontsize': 16, 'color': '#d1d1d1', 'fontweight': 'bold'}


class Matplot:

    def __init__(self, x, y, plots, fontdict=None):
        if fontdict is None:
            fontdict = FONTDICS
        else:
            self.fontdict = fontdict
        self.x = x
        self.y = y
        self.plots = plots

    def draw(self):
        types = ['b.-', 'r.-', 'g.-']  # type plot chart
        plt.title('TESTING', fontdict=self.fontdict)  # title and font config
        for idx, dt in enumerate(self.plots):
            # TODO: multple plot
            plt.plot(self.x, self.y[idx], types[idx], label=dt)  # plot data

        # TODO: how to show legends.
        plt.xlabel('Time')
        plt.ylabel('Dolar')
        # TODO show label with label in plot
        plt.legend()
        # TODO show chart
        plt.show()
