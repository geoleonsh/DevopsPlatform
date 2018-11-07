from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length


class LoginForm(FlaskForm):
    UserName = StringField('用户名', validators=[DataRequired(message='用户名必填'), Length(5, 20, message='用户名长度为6到20之间')],
                           render_kw={"class": "form-control"})
    PassWord = PasswordField('密码', validators=[DataRequired(message='密码必填'), Length(6, 20, message='密码长度为8到20之间')],
                             render_kw={"class": "form-control"})
    Submit = SubmitField('登录', render_kw={"class": "btn btn-primary"})


class BranchForm(FlaskForm):
    Yicunh5 = StringField('yicunh5分支')
