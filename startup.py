from flask import Flask, render_template, redirect, url_for, flash
from forms import LoginForm
from config import MainConfig
from validation import Validation
from flask_login import LoginManager

app = Flask(__name__, template_folder='templates')
app.config.from_object(MainConfig)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    validation = Validation()
    if form.validate_on_submit():
        username = form.UserName.data
        password = form.PassWord.data
        if validation.login_validation(username, password):
            return redirect(url_for('index'))
        else:
            flash("用户名或密码错误!")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
