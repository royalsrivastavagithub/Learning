def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("Sprinkled !")
        func(*args, **kwargs)
    return wrapper

def add_sugar(func):
    def wrapper(*args, **kwargs):
        print("Sugar Added !")
        func(*args, **kwargs)
    return wrapper

@add_sugar
@add_sprinkles
def get_ice_cream(flavor):
    print(f"{flavor} Ice Cream")


get_ice_cream("vanilla")