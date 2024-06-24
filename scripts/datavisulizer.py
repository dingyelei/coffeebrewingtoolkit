
class DataVisualizer:

    @staticmethod
    def get_data_visualizer(**param):    
        data_visualizer = None
        match param['data_visualizer']:
            case 'Matplotlib': 
                data_visualizer = DataVisualizerMatplotlibAdapter()
        return data_visualizer

    def __init__(self):
        self.name = "Abstract Data Visualizer"

    def __str__(self):
        return self.name
    
    def brewing_chart(self, **param):
        raise Exception("method not implemented")

import matplotlib.pyplot as plt
import numpy as np
import time

class DataVisualizerMatplotlibAdapter(DataVisualizer):
    def __init__(self):
        self.name = "Matplotlib Data Visualizer"

    def brewing_chart(self, **param):

        print('build brewing chart')
        plt.style.use('_mpl-gallery')

        # make the data
        np.random.seed(3)
        x = 4 + np.random.normal(0, 2, 8)
        y = 4 + np.random.normal(0, 2, len(x))
        # size and color:
        sizes = np.random.uniform(15, 80, len(x))
        colors = self.render_color(len(x))
        # plot
        fig, ax = plt.subplots()

        ax.scatter(x, y, s=sizes, c=colors, vmin=0, vmax=100)
        ax.set(xlim=(0, 8), xticks=np.arange(1, 8),
            ylim=(0, 8), yticks=np.arange(1, 8))
        plt.show()

    def render_color(self, size):
        np.random.seed(seed=int(time.time()))
        rgb = np.random.uniform(0, 1, 3)
        color_change = lambda x: x + 0.125 if x + 0.125 < 1 else x + 0.125 - 1
        colors = []
        for i in range(size):
            rgb = [color_change(rgb[0]), rgb[1], rgb[2]]
            colors.append(rgb)
        return colors     
