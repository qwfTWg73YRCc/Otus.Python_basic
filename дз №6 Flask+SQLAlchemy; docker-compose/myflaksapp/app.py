from flask import Flask, request, render_template, redirect
from flask_migrate import Migrate

import config
# from views import product_app
from models import db

app = Flask(__name__)
app.config.update(
    SQLALCHEMY_DATABASE_URI=config.SQLALCHEMY_DATABASE_URI,
)
# app.register_blueprint(product_app, url_prefix="/products")


db.init_app(app)  # инициализация происходит до миграции (снизу)
# изменилось то, что db создалось в другом месте, а потом импортировано в app.py
migrate = Migrate(app, db)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/userrequest', methods=['POST', 'GET'])
def user_request():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        email = request.form['email']
        userrequest = Request(name=name, phone=phone, email=email)
        try:
            db.session.add(userrequest)
            db.session.commit()
            return redirect('user-requests.html')
        except:
            return "Error"
    else:
        return render_template('userrequest.html')


@app.route('/user-requests')
def about():
    requests = Request.query.all()
    return render_template('user-requests.html', requests=requests)

