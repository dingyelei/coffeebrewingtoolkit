
class Coffee:

    def __init__(self, **param):
        self.id = param['id']
        self.country = param['country']
        self.region = param['region']
        self.producer = param['producer']
        self.cultivar = param['cultivar']
        self.process = param['process']
        self.roaster = param['roaster']
        self.roast_date = param['roast_date']
        self.bag_size = param['bag_size']
        self.price = param['price']
        self.flavors = param['flavors']
        self.image_note = param['image_url']
        self.agtron = param['agtron']
        self.comments = param['comments']
        self.barista_id = param['barista_id']

    def __str__(self):
        return f"{self.id}: {self.roaster}\n  {self.cultivar} by {self.producer},{self.region}, {self.country}\n  roasted on {self.roast_date}, ¥{self.price}/{self.bag_size}g\n  flavor notes: {self.flavors}"

class Barista:
    def __init__(self, **param):
        self.id = param['id']
        self.name = param['name']
        self.email = param['email']
        self.password = param['password']
        self.join_community_date = param['created_date']

    def __str__(self):
        return f"Barista #{self.id} '{self.name}' created on {self.join_community_date}"

from time import strftime
from time import gmtime
class Brewing:
    @staticmethod
    def group_by(brewings, group_by_keyword):
        data = {}
        for brewing in brewings:
            group_by_id = brewing.__dict__[group_by_keyword]
            data[group_by_id] = data.get(group_by_id, []) + [brewing]
        return data

    def __init__(self, **param):
        self.id = param['id']
        self.brewing_date = param['brewing_date']
        self.water_temperature = param['water_temperature']
        self.ratio = param['ratio']
        self.mass_of_coffee = param['mass_of_coffee']
        self.mass_of_water = param['mass_of_water']
        self.grinder = param['grinder']
        self.grind_size = param['grind_size']
        self.dripper = param['dripper']
        self.brewing_method = param['brewing_method']
        self.brewing_time = param['brewing_time']
        self.mass_of_beverage = param['mass_of_beverage']
        self.tds = param['tds']
        self.pe = param['pe']
        self.coffee_id = param['coffee_id']
        self.barista_id = param['barista_id']
        
        self.pe = self.mass_of_beverage * self.tds / self.mass_of_coffee

    def __str__(self):
        tds = "{:.2f}".format(self.tds)
        pe = "{:.2f}".format(self.pe)
        return f"Brewing details #{self.id} by barista-{self.barista_id} on {self.brewing_date}\n  {self.ratio}, w/ {self.grinder} #{self.grind_size}, water temp.{self.water_temperature}°C\n  TDS:{tds}% PE:{pe}%"
    
    def thumbnail(self):
        brewing_time = strftime("%M'%S''", gmtime(self.brewing_time))
        return f"Coffee #{self.coffee_id} - Brewing #{self.id}: {self.ratio}, {self.grinder} #{self.grind_size}, {self.dripper}, {brewing_time}"


if __name__ == '__main__':
    param = {
        'id': 16,
        'name': 'yelei',
        'email': 'yelei@coffeecompany.com',
        'password': '1qaz2wsx',
        'join_community_date': '2024-07-23',
    }
    yelei = Barista(**param)
    print(yelei)