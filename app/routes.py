from flask import flash, render_template, request, Markup
from app import app
from app.forms import CarChoiceForm, SearchForm
from app.controllers import CARS, find_car, car_by_name


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        transmission = request.form['transmission'] \
            if 'transmission' in request.form else None
        volume = request.form['volume'] \
            if 'volume' in request.form else None
        conditioner = request.form['conditioner'] \
            if 'conditioner' in request.form else None

        search_result = find_car(
            transmission=transmission,
            volume=volume,
            is_conditioner=conditioner
        )
        return render_template("search.html", form=SearchForm(),
                               cars=search_result)
    return render_template("index.html", form=SearchForm(), cars=CARS)


@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        transmission = request.form['transmission']
        volume = request.form['volume']
        conditioner = request.form['conditioner']

        search_result = find_car(
            transmission=transmission,
            volume=volume,
            is_conditioner=conditioner
        )
        return render_template("search.html", form=SearchForm(),
                               cars=search_result)
    return render_template("search.html", form=SearchForm(), cars={})


@app.route('/cars/<string:car_name>', methods=['GET', 'POST'])
def car_page(car_name):
    error = False
    error_message = "<div class='container border border-1" \
                    "rounded pt-2 pb-2 mt-3 bg-danger' style='width:40rem;'>" \
                    "<h5 class='text-white'>Ошибка:</h5>"
    car = car_by_name(car_name)
    if request.method == 'POST':
        name = request.form['name']
        last_name = request.form['last_name']
        telephone = request.form['telephone']
        order_date = request.form['order_date']

        if not name:
            error_message += "<h6 class='text-white'>- заполните имя</h6>"
            error = True
        elif not name.isalpha():
            error_message += "<h6 class='text-white'>- " \
                             "имя должно состоять из букв</h6>"
            error = True
        if not last_name:
            error_message += "<h6 class='text-white'>- " \
                             "заполните фамилию</h6>"
            error = True
        elif not last_name.isalpha():
            error_message += "<h6 class='text-white'>- " \
                             "фамилия должна состоять из букв</h6>"
            error = True
        if not telephone:
            error_message += "<h6 class='text-white'>- " \
                             "заполните телефон</h6>"
            error = True
        elif not telephone.isdigit():
            error_message += "<h6 class='text-white'>- " \
                             "телефон должен состоять из цифр</h6>"
            error = True
        if not order_date:
            error_message += "<h6 class='text-white'>- " \
                             "заполните дату аренды</h6>"
            error = True
        elif order_date.isalnum():
            error_message += "<h6 class='text-white'>- " \
                             "дата должна быть в формате '2021-09-15'</h6>"
            error = True

        error_message += "</div>"

        if error:
            flash(Markup(error_message))
        else:
            flash(Markup(f"<div class='container border border-1 "
                         f"rounded pt-2 pb-2 mt-3 bg-success' "
                         f"style='width:40rem;'>"
                         f"<h5 class='text-white'>Автомобиль {car['name']} "
                         f"забронирован:</h5>"
                         f"<h6 class='text-white'>дата - {order_date}</h6>"
                         f"<h6 class='text-white'>имя - {name}</h6>"
                         f"<h6 class='text-white'>фамилия - {last_name}</h6>"
                         f"<h6 class='text-white'>телефон - +{telephone}</h6>"
                         f"</div>"))

        return render_template("car.html", car=car, form=CarChoiceForm())

    car["transmission"] = "автоматическая" if car["transmission"] == "auto"\
        else "механическая"
    car["volume"] = str(car["volume"])
    car["is_conditioner"] = "есть" if car["is_conditioner"] is True else "нет"

    return render_template("car.html", car=car, form=CarChoiceForm())
