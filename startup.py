#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for, flash
from flask_login import LoginManager, login_required, current_user, login_user
from config import MainConfig
from forms import LoginForm
from user import User

app = Flask(__name__, template_folder='templates')
app.config.from_object(MainConfig)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = '请先进行登录'


@login_manager.user_loader
def load_user(userid):
    return User.get(userid)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if not current_user.is_anonymous:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        username = form.UserName.data
        password = form.PassWord.data
        user = User(username)
        if user.is_matched(username, password):
            login_user(user, remember=True)
            return redirect(url_for('index'))
        else:
            flash("用户名或密码错误!")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/')
@login_required
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
