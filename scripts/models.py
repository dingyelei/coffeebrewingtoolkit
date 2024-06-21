from datetime import datetime
from datetime import timedelta

class CoffeeRepository:

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
        self.image_note = param['image_note']
        self.agtron = param['agtron']
        self.comments = param['comments']

    def __str__(self):
        return f"{self.id}: {self.roaster}\n  {self.cultivar} by {self.producer},{self.region}, {self.country}\n  roasted on {self.roast_date}, ¥{self.price}/{self.bag_size}g\n  flavor notes: {self.flavors}"

class Barista:
    def __init__(self, **param):
        self.id = param['id']
        self.name = param['name']
        self.email = param['email']
        self.join_community_date = param['join_community_date']

    def __str__(self):
        return f"Barista #{self.id} '{self.name}' joined community on {self.join_community_date}"
    
class Brewings:
    def __init__(self, **param):
        self.id = param['id']
        self.brewing_date = param['brewing_date']
        self.temperature = param['temperature']
        self.ratio = param['ratio']
        self.dose = param['dose']
        self.water = param['water']
        self.grinder = param['grinder']
        self.grinding_size = param['grinding_size']
        self.dripper = param['dripper']
        self.brewing_method = param['brewing_method']
        self.brewing_time = param['brewing_time']
        self.coffee = param['coffee']
        self.tds = param['tds']
        self.pe = param['pe']
        self.coffee_id = param['coffee_id']
        self.barista_id = param['barista_id']


    def __str__(self):
        return f"Brewing details #{self.id} by barista-{self.barista_id}"