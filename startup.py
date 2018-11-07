#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from config import MainConfig
from forms import LoginForm
from user import User

app = Flask(__name__, template_folder='templates')
app.config.from_object(MainConfig)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
login_manager.login_message = '请先进行登录'
view = 'default'


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
            global view
            view = 'default'
            return redirect(url_for('index'))
        else:
            flash("用户名或密码错误!")
            return redirect(url_for('login'))

    return render_template('login.html', form=form)


@app.route('/')
@login_required
def index():
    return render_template('index.html', view=view)


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/action/')
@login_required
def action():
    global view
    operation = request.args.get('operation')
    if operation == 'webbranch':
        view = 'webbranch'
        return redirect(url_for('index'))
    elif operation == 'java':
        view = 'preview'
        return redirect(url_for('index'))
    elif operation == 'listuser':
        view = 'preview'
        return redirect(url_for('index'))
    elif operation == 'adduser':
        view = 'preview'
        return redirect(url_for('index'))
    elif operation == 'deluser':
        view = 'preview'
        return redirect(url_for('index'))
    elif operation == 'modifyuser':
        view = 'preview'
        return redirect(url_for('index'))
    elif operation == 'authority':
        view = 'preview'
        return redirect(url_for('index'))
    elif operation == 'grant':
        view = 'preview'
        return redirect(url_for('index'))


@app.route('/deal/')
@login_required
def deal():
    action = request.args.get('action')
    value = request.args.get('value')
    if action == 'get':
        pass
    if action == 'change':
        pass


if __name__ == '__main__':
    app.run(debug=True)
