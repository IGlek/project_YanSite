from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    id_user = StringField('Id астронавта', validators=[DataRequired()])
    pas_user = PasswordField('Пароль астронавта', validators=[DataRequired()])
    id_cap = StringField('Id капитана', validators=[DataRequired()])
    pas_cap = PasswordField('Пароль капитана', validators=[DataRequired()])
    # remember_me = BooleanField('Запомнить меня') <p>{{ form.remember_me() }} {{ form.remember_me.label }}</p>
    submit = SubmitField('Доступ')


