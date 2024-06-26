from dataexchange import DataExchange
from datavisulizer import DataVisualizer

class CoffeeCommunity:
    def __init__(self, **param):
        self.data_exchange = DataExchange(**param)
        self.data_visualizer = DataVisualizer.get_data_visualizer(**param)
    
    def brewing_chart(self, **param):
        self.data_visualizer.brewing_chart(**param)


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
    param = brewings | cc.data_visualizer.defaults
    cc.brewing_chart(**param)
    