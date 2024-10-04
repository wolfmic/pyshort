"""
Flask Application to shorten links and register them to redis
"""


import os
from flask import Flask, request, redirect, url_for, flash
from flask.templating import render_template
from hashids import Hashids
import redis


app = Flask(__name__)

redis_db = redis.StrictRedis(
    host=os.getenv("REDIS_HOST", "127.0.0.1"),
    port=6379,
    db=0,
    )

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'secret salt')

hashids = Hashids(min_length=4, salt=app.config['SECRET_KEY'])
redis_db.set('count', 0)

@app.route("/", methods=('GET', 'POST'))
def index():
    """
    Main Page
    """

    if request.method == 'POST':
        url_id = redis_db.get('count')
        url_id = int.from_bytes(url_id, "big")
        print(f'{url_id}')
        redis_db.set(f'url:{url_id}', request.form['url'])
        redis_db.incr('count')
        hashid = hashids.encode(url_id)
        request.base_url = request.base_url.replace("http://", "https://")
        short_url = request.base_url + hashid
        return render_template('index.html', short_url=short_url)

    return render_template('index.html')

@app.route('/<url_id>')
def url_redirect(url_id):
    """
    Catch any url after as an ID an redirect it
    """

    original_id = hashids.decode(url_id)
    if original_id:
        original_id = original_id[0]
        original_url = redis_db.get(f'url:{original_id}').decode('utf-8')
        return redirect(original_url)

    flash('Invalid URL')
    return redirect(url_for('index'))
