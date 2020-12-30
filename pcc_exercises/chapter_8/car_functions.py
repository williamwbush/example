def car_info(manufacturer, model, **other_info):
    """makes a dictionary of info about a car"""
    car_dict = {}
    car_dict["Manufacturer"] = manufacturer
    car_dict["Model"] = model
    for key, value in other_info.items():
        car_dict[key] = value
    return car_dict