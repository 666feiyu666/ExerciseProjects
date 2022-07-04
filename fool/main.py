class Restaurant:

    def __init__(self,restaurant_name,cuisine_type):
        self.name=restaurant_name
        self.type=cuisine_type

    def describe_restaurant(self):
        return f"The name of the restaurant is {self.name}. It provides {self.type} food."

    def open_restaurant(self):
        print("The restaurant is open!")

wangshengtang = Restaurant('wangshengtang','Chinese')
print(wangshengtang.describe_restaurant())