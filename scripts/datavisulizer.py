
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

    def render_color(self, size):
        np.random.seed(seed=int(time.time()))
        rgb = np.random.uniform(0, 1, 3)
        color_change = lambda x: x + 0.125 if x + 0.125 < 1 else x + 0.125 - 1
        colors = []
        for i in range(size):
            rgb = [color_change(rgb[0]), rgb[1], rgb[2]]
            colors.append(rgb)
        return colors     
