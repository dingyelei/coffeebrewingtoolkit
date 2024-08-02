from models import Brewing

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
    
    def box_chart(self, **param):
        raise Exception("method not implemented")

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import time
import statistics

class DataVisualizerMatplotlibAdapter(DataVisualizer):
    def __init__(self):
        self.name = "Matplotlib Data Visualizer"
        self.defaults = {
            'markers': ["o", ">", "p", "*", "H"],
            'label_loc': 'upper right',
            'label_font_size': 9,
            'label_spacing': 0.8,
            'patch_line_width': 4,
            'patch_edge_color': '0.5',
            'subplot_title': 'Coffee Brewing Control Chart',
            'y_span': 0.05,
            'y_limits_left': 1.0,
            'y_limits_right': 1.8,
            'y_format': '{x:.2f}',
            'y_label': 'STRENGTH | Solubles Concentration - %', 
            'x_span': 0.5,
            'x_limits_left': 15,
            'x_limits_right': 21,
            'x_format': '{x:.2f}',
            'x_label': 'EXTRACTION | Solubles Yield - %', 
            'grid_line_style': "--",
            'grid_line_width': 0.25,
            'grid_color': '.25',
            'marker_size': 11,
            'box_plot_group_by': 'dripper',
            'box_plot_weight': 'tds',
            'figure_height':6.6,
            'figure_width':8.8,
        }

    def box_chart(self, **param):
        group_by_keyword = param['box_plot_group_by']
        brewings = param['data_brewings']
        brewing_groups = Brewing.group_by(brewings, group_by_keyword)

        x_labels = brewing_groups.keys()
        weights = [ [brewing.__dict__[param['box_plot_weight']] for brewing in brewing_groups[x_label]] for x_label in x_labels]
        
        print('build box chart for brewing comparison.')
        fig, ax = plt.subplots()
        fig.set_figheight(param['figure_height'])
        fig.set_figwidth(param['figure_width'])
        ax.set_title(param['subplot_title'], weight='bold')
        ax.grid(linestyle=param['grid_line_style'], linewidth=param['grid_line_width'], color=param['grid_color'])

        param['ax'] = ax
        self.y_axis_setup(**param)

        boxplot = ax.boxplot(weights, patch_artist=True, tick_labels=x_labels)
        
        colors = self.render_color(len(x_labels))
        for patch, color in zip(boxplot['boxes'], colors):
            patch.set_facecolor(color)
        
        legend_labels = [f"{label}: {"{:.2f}".format(statistics.mean(weight))}"for weight, label in zip(weights, x_labels)]
        ax.legend(loc=param['label_loc'], fontsize=param['label_font_size'], labelspacing=param['label_spacing'], labels=legend_labels)
        
        fig.patch.set(linewidth=param['patch_line_width'], edgecolor=param['patch_edge_color'])
        plt.show()
        
    def brewing_chart(self, **param):
        print('build brewing chart.')
        fig, ax = plt.subplots()
        fig.set_figheight(param['figure_height'])
        fig.set_figwidth(param['figure_width'])
        ax.set_title(param['subplot_title'], weight='bold')
        ax.grid(linestyle=param['grid_line_style'], linewidth=param['grid_line_width'], color=param['grid_color'])

        param['ax'] = ax
        self.x_axis_setup(**param)
        self.y_axis_setup(**param)

        brewings = param['data_brewings']
        colors = self.render_color(len(brewings))
        for brewing, color in zip(brewings, colors):
            ax.plot(param['x_axis'], param['y_axis'], data=brewing.__dict__,
                    marker=self.render_marker(), markersize=param['marker_size'], color=color,
                    label=brewing.thumbnail())
        
        ax.legend(loc=param['label_loc'], fontsize=param['label_font_size'], labelspacing=param['label_spacing'])
        fig.patch.set(linewidth=param['patch_line_width'], edgecolor=param['patch_edge_color'])
        plt.show()

    def x_axis_setup(self, **param):
        ax = param['ax']
        ax.set_xlabel(param['x_label'], weight='bold')
        ax.set_xlim(param['x_limits_left'], param['x_limits_right'])
        ax.xaxis.set_major_locator(MultipleLocator(param['x_span']))
        ax.xaxis.set_minor_formatter(param['x_format'])

    def y_axis_setup(self, **param):
        ax = param['ax']
        ax.set_ylabel(param['y_label'], weight='bold')
        ax.set_ylim(param['y_limits_left'], param['y_limits_right'])
        ax.yaxis.set_major_locator(MultipleLocator(param['y_span']))
        ax.yaxis.set_minor_formatter(param['y_format'])

    def render_marker(self):
        np.random.seed(seed=int(time.time()))
        idx = int(np.random.uniform(0, len(self.defaults['markers'])))
        return self.defaults['markers'][idx]
                            
    def render_color(self, size):
        np.random.seed(seed=int(time.time()))
        rgb = np.random.uniform(0, 1, 3)
        color_change = lambda x: x + 0.125 if x + 0.125 < 1 else x + 0.125 - 1
        colors = []
        for i in range(size):
            rgb = [color_change(rgb[0]), color_change(rgb[1]), color_change(rgb[2])]
            colors.append(rgb)
        return colors     
