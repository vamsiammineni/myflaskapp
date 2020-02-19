import os
from flask import Flask, request, redirect, url_for, render_template
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient(os.environ['MYFLASKAPP_DB_1_PORT_27017_TCP_ADDR'], 27017)
db = client.itemsdb


@app.route('/')
def homepage():
    items = db.itemsdb.find()
    items = [item for item in items]
    return render_template('base.html', items=items)


@app.route('/new', methods=['POST'])
def new():
    items_doc = {'name': request.form['name'],
                 'description': request.form['description']
                 }
    db.itemsdb.insert_one(items_doc)
    return redirect(url_for('homepage'))


@app.route('/hello')
def hello():
    return 'Hello everyone!!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


