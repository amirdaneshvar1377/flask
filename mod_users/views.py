from . import users
from flask import request, session, render_template, flash
from .forms import RegisterForm
from app import db
from .models import User
from sqlalchemy.exc import IntegrityError

@users.route("/register/", methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if not form.validate_on_submit():
            return render_template("users/register.html", form=form)
        if not form.password.data == form.password_confirm.data:
            error_msg = 'Password and Confirm Password does not match'
            form.password.errors.append(error_msg)
            form.password_confirm.errors.append(error_msg)
            return render_template('users/register.html', form=form)
        new_user = User()
        new_user.full_name = form.full_name.data
        new_user.email = form.email.data
        new_user.set_password(form.password.data)
        try:
            db.session.add(new_user)
            db.session.commit()
            flash("You Created your account successfully", category='succe3ss')
        except IntegrityError:
            db.session.rollback()
            flash("Email is in use", category='error')
    return render_template("users/register.html", form=form)