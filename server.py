from flask import Flask, render_template, redirect
from loginform import LoginForm
    

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route('/')
@app.route('/index')
def index(label):
    param = {'label': 'И на Марсе будут яблони цвести!', 'title': label}
    return render_template('index.html', **param)


@app.route('/training/<prof>')
def training(prof):
    param = {'title': "Тренировки в полёте", "spec": prof}
    return render_template('training.html', **param)


@app.route('/list_prof/<var>')
def list_prof(var):
    param = {'title': "Список профессий", "var": var}
    return render_template('list_prof.html', **param)


@app.route('/answer')
@app.route('/auto_answer')
def answer():
    param = {'title': "Анкета", 'surname': "Фёдоров", 'name': "Марк", 'education': "Среднее", 'profession': " Писатель",
             'sex': "Male", 'motivation': "Распространить хип-хоп в космос!", 'ready': "True"}
    return render_template('auto_answer.html', **param)


@app.route('/login', methods=['GET', 'POST'])
def login():
    param = {'title': "Аварийный доступ"}
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', **param, form=form)


@app.route('/distribution')
def success():
    param = {'title': "По каютам!", "users": ['Ридли Скотт', 'Энди Уир', 'Марк Уотни', "Венката Капур",
                                              'Тедди Сандерс', 'Шон Бин']}
    return render_template('distribution.html', **param)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
