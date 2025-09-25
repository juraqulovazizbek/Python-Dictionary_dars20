car = {
    "brand": "Chevrolet",
    "model": "Cobalt",
    "color": "white"
    }
brand = car["brand"]

color = car["color"]
year = car.get('year', 2025)
print(brand, color, year)