import matplotlib.pyplot as plt
import constants


class Plot:

    def __init__(self, x, y, plots, title=None, fontdict=None):  # TODO Fontdict is option pass
        # TODO: pass default value for optional parameter
        if fontdict is None:
            self.fontdict = constants.FONTDICS
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
