from dataexchange import DataExchange
from datavisulizer import DataVisualizer

class CoffeeToolkit:
    def __init__(self, **param):
        self.data_exchange = DataExchange(**param)
        self.data_visualizer = DataVisualizer.get_data_visualizer(**param)
    
    def brewing_chart(self, **param):
        self.data_visualizer.brewing_chart(**param)

    def box_chart(self, **param):
        self.data_visualizer.box_chart(**param)


if __name__ == '__main__':
    cc = CoffeeToolkit(
        data_accessor = "SQLite",
        db_file = "...coffee_company.db",
        data_visualizer = "Matplotlib"
    )

    coffees = cc.data_exchange.get_coffees(id=4)
    for coffee in coffees:
        print(coffee)

    data = []
    for brewing in cc.data_exchange.get_brewings():
        if brewing.coffee_id == 4:
            data.append(brewing)

    brewings = {
        'data_brewings': data,
        'x_axis': 'pe',
        'y_axis': 'tds',
        'y_span': 0.05,
        'y_limits_left': 1.30,
        'y_limits_right': 1.90,
        }
    param = cc.data_visualizer.defaults | brewings
    cc.brewing_chart(**param)
    
    brewing_groups = {
        'data_brewings': data,
        'subplot_title': 'Box Plot for Brewing Factor Comparison',
        'box_plot_group_by': 'grind_size',
        'y_span': 0.025,
        'y_limits_left': 1.45,
        'y_limits_right': 1.6,
    }
    param = cc.data_visualizer.defaults | brewing_groups
    # cc.box_chart(**param)
    