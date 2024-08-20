import matplotlib.pyplot as plt
import constants


class Pie:

    def __init__(self, values, colors, labels,  title=None, font_dict=None):  # TODO Font dict is option pass
        # TODO: pass default value for optional parameter
        if font_dict is None:
            self.font_dict = constants.FONTDICS
        else:
            self.font_dict = font_dict
        self.values = values
        self.colors = colors
        self.labels = labels
        self.title = title

    def draw(self):
        plt.title = self.title
        plt.pie(self.values, labels=self.labels, colors=self.colors, startangle=90)
        plt.legend(loc='best')
        plt.show()


