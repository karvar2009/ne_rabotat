from app import app
from flask import request, render_template
import datetime
import requests


@app.route('/')
def index():
    return render_template('index.html', current_time=datetime.datetime.utcnow())


@app.route('/github-search', methods=['GET', 'POST'])
def github_search():
    if request.method == 'POST':
        lang = request.form.get('lang')
        sort = request.form.get('sort')
        url = 'api.github.com/search/repositories'
        parameters = {
            'q': f'language:{lang}',
            'sort': f'sort={sort}'
        }
        response = requests.get(url, parameters)
        response_json = response.json()
        result = response_json['items']
        return render_template('github.html', repositories=result)


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
        lang = request.form.get('lang')
        width = request.form.get('width')
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
