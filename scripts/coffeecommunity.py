from dataexchange import DataExchange
from datavisulizer import DataVisualizer

class CoffeeCommunity:
    def __init__(self, **param):
        self.data_exchange = DataExchange(**param)
        self.data_visualizer = DataVisualizer.get_data_visualizer(**param)
    
    def brewing_chart(self, **param):
        self.data_visualizer.brewing_chart(**param)

    def box_chart(self, **param):
        self.data_visualizer.box_chart(**param)


if __name__ == '__main__':
    cc = CoffeeCommunity(
        data_accessor = "SQLite",
        db_file = ".../example.db",
        data_visualizer = "Matplotlib"
    )
    brewings = {
        'data_brewings': cc.data_exchange.get_brewings('brewings'),
        'x_axis': 'pe',
        'y_axis': 'tds',
        }
    param = cc.data_visualizer.defaults | brewings
    cc.brewing_chart(**param)
    
    brewing_groups = {
        'data_brewings': cc.data_exchange.get_brewings('brewings'),
        'subplot_title': 'Box Plot for Brewing Factor Comparison',
        'y_span': 0.025,
        'y_limits_left': 1.25,
        'y_limits_right': 1.375,
    }
    param = cc.data_visualizer.defaults | brewing_groups
    #cc.box_chart(**param)
    