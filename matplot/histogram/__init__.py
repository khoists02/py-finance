from matplotlib import pyplot as plt


class Histogram:
    def __init__(self, x, bins, xlabel, ylabel, title, legend=None):
        self.x = x
        self.bins = bins
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        if legend is None:
            self.legend = []
        else:
            self.legend = legend

    def draw(self):
        plt.figure(figsize=(10, 5))
        plt.hist(self.x, bins=self.bins)
        plt.xlabel(self.xlabel)
        plt.ylabel(self.ylabel)
        plt.title(self.title)
        plt.xticks(self.bins)
        plt.show()
