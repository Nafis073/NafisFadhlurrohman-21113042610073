def build_car(manufacturer, model, **car_info):
    car_info["manufacturer"] = manufacturer
    car_info["model"] = model

    return car_info

car = build_car(
    "Toyota",
    "Avanza",
    color="Hitam",
    year=2024,
    transmission="Manual"
)

print(car)