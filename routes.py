from app import app
from flask import request, render_template


@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    menu = [
        {'name': 'Главная', 'url': index},
        {'name': 'Я на ТыТруба', 'url': 'https://www.youtube.com/channel/UC6zzr4UN1ECuaOP66TTuNHw'}
    ]
    return render_template('base.html', context=menu)


@app.route('/user/<username>')
def user(username):
    return f'<h1>Привет, {username}</h1>'


@app.route('/query-example')
def query_example():
    lang = request.args.get('language')
    languages = {

    }
    return f'Ваш язык: {lang}'


@app.route('/form-example', methods=['GET', 'POST'])
def form_example():
    if request.method == 'POST':
        lang = request.args.get('lang')
        width = request.args.get('width')
        print(lang)
        print(width)
        return render_template('form.html', context=[lang, width])
    return render_template('form.html')


@app.route('/json-example')
def json_example():
    return None


@app.route('/about')
def about():
    return None


@app.errorhandler(404)
def not_found_404(error):
    return render_template('404.html'), 404
