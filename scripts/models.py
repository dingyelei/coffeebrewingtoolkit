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

