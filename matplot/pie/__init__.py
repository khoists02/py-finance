import matplotlib.pyplot as plt
import constants


class Pie:

    def __init__(self, values, colors, labels,  title=None, fontdict=None):  # TODO Fontdict is option pass
        # TODO: pass default value for optional parameter
        if fontdict is None:
            self.fontdict = constants.FONTDICS
        else:
            self.fontdict = fontdict
        self.values = values
        self.colors = colors
        self.labels = labels
        self.title = title

    def draw(self):
        plt.title = self.title
        plt.pie(self.values, labels=self.labels, colors=self.colors, startangle=90)
        plt.legend(loc='best')
        plt.show()


