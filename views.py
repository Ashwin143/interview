from flask import render_template, request
from models import Dessert, create_dessert
from app import app


@app.route('/enquiries')
def index():

    desserts = Dessert.query.all()

    return render_template('index.html', desserts=desserts)


@app.route('/forms', methods=['GET', 'POST', 'DELETE'])
def add():

    if request.method == 'GET':
        return render_template('add.html')

    dessert_name = request.form.get('name_field')
    dessert_price = request.form.get('price_field')
    dessert_cals = request.form.get('cals_field')
    dessert_sub = request.form.get('Subject_field')
    sex = request.form['options']

    dessert = create_dessert(dessert_name, dessert_price, dessert_cals,
                             dessert_sub, sex)
    return render_template('add.html', dessert=dessert)


@app.route('/enquiry/<id>', methods=['GET', 'POST'])
def show_post(id):
    # return getthings(name_id)
    d = Dessert.query.filter_by(id=id).first_or_404()
    t = []
    t.append(d.name)
    t.append(d.email)
    t.append(d.MobileNumber)
    t.append(d.Subject)
    t.append(d.sex)

    # return render_template('index.html', d=d)
    return str(t)

    # return int(dessert1)
