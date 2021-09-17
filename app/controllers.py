CARS = (
    {'name': 'Volkswagen Golf',
     'link_name': 'vw_golf',
     'transmission': 'auto',
     'volume': 1.4,
     'is_conditioner': True,
     'image_path': 'static/images/vw_golf.jpg'},
    {'name': 'Seat Ibiza',
     'link_name': 'seat_ibiza',
     'transmission': 'manual',
     'volume': 1.0,
     'is_conditioner': False,
     'image_path': 'static/images/seat_ibiza.jpg'},
    {'name': 'Lexus GS 350',
     'link_name': 'lexus_gs_350',
     'transmission': 'auto',
     'volume': 3.5,
     'is_conditioner': True,
     'image_path': 'static/images/lexus_gs350.jpg'},
    {'name': 'Ford Mustang',
     'link_name': 'ford_mustang',
     'transmission': 'manual',
     'volume': 2.3,
     'is_conditioner': True,
     'image_path': 'static/images/ford_mustang.jpg'},
    {'name': 'Toyota Tundra',
     'link_name': 'toyota_tundra',
     'transmission': 'auto',
     'volume': 5.7,
     'is_conditioner': False,
     'image_path': 'static/images/toyota_tundra.jpg'},
    {'name': 'Mercedes-Benz G 65 AMG',
     'link_name': 'mb_g_65_amg',
     'transmission': 'auto',
     'volume': 6.0,
     'is_conditioner': True,
     'image_path': 'static/images/mb_g65.jpg'}
)


def find_car(transmission, volume, is_conditioner):
    transmission = transmission if transmission else ("auto", "manual")
    volume = float(volume) if volume else 1.0
    is_conditioner = \
        (bool(is_conditioner),) if is_conditioner is not None else (True, False)

    result = []
    for car in CARS:
        if car["transmission"] in transmission \
                and car["volume"] >= volume \
                and car["is_conditioner"] in is_conditioner:
            result.append(car)
    return result


def car_by_name(name: str):
    for car in CARS:
        if car["link_name"] == name:
            return car
