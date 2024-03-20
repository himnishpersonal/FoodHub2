import requests

class Restaurant:
    def __init__(self, id_restaurant, name, locale):
        self.id_restaurant = id_restaurant
        self.name = name
        self.locale = locale
        
    def __repr__(self):
        return f"Restaurant(id_restaurant={self.id_restaurant}, name='{self.name}', locale='{self.locale}')"
    
class MyRestClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.host = 'ieCqIDSYqdh2Cmi222wwGVAJYBCCiEa1VHazzL6YvC7_Ex2fUIKWNI4bfO8QLAPpjVE3qjV6zzurSONBaL3QdRitMKqi9m74F910mknmbOc49KE9JWPiRgoUGadRZHYx'