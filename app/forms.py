from flask_wtf import FlaskForm
from wtforms import BooleanField, DateField, FloatField,\
    IntegerField, RadioField, StringField, SubmitField
from wtforms.validators import InputRequired, NumberRange, Regexp


class SearchForm(FlaskForm):
    transmission = RadioField(choices=(("auto", "автоматическая"),
                                       ("manual", "механическая")))
    volume = FloatField(validators=[
        InputRequired(message="поле не может быть пустым"),
        NumberRange(min=1, max=5,
                    message="вы можете установить значение от 1 до 5")],
        render_kw={"placeholder": "1.0"})
    conditioner = BooleanField()
    submit = SubmitField(label="Поиск")


class CarChoiceForm(FlaskForm):
    name = StringField(validators=[
        InputRequired(message="поле не может быть пустым"),
        Regexp(regex=r"[А-Я][а-я]+",
               message="имя должно быть написано"
                       "на русском языке с заглавной буквы")],
        render_kw={"placeholder": "Имя"}
    )
    last_name = StringField(validators=[
        InputRequired(message="поле не может быть пустым"),
        Regexp(regex=r"[А-Я][а-я]+",
               message="фамилия должна быть написана"
                       "на русском языке с заглавной буквы")],
        render_kw={"placeholder": "Фамилия"}
    )
    telephone = IntegerField(validators=[
        NumberRange(min=11, max=15,
                    message="номер должен быть длиной"
                            "от 11 до 15 символов и включать код")
    ],
        render_kw={"placeholder": "78005555505"}
    )
    order_date = DateField(validators=[InputRequired(
        message="поле не может быть пустым")],
        render_kw={"placeholder": "2021-09-15"}
    )
    submit = SubmitField(label="Забронировать")

