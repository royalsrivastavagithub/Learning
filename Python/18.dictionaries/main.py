#dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United States": "Washington D.C.",
    "United Kingdom": "London",
    "Canada": "Ottawa",
    "Brazil": "Brasilia",
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Colombia": "Bogota",
    "Mexico": "Mexico City",
    "Peru": "Lima",
    "Venezuela": "Caracas",
    "Ecuador": "Quito",
    "India": "New Delhi",
    "Pakistan": "Islamabad",}

capitals.pop("Pakistan")

for keys, values in capitals.items():
    print(f"The capital of {keys} is {values}")

keys = list(capitals.keys())
values = capitals.values()
print(keys)
print(values)

print(type(keys))
print(type(values))