from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextField, SelectMultipleField
from wtforms.validators import DataRequired


class CreatePostForm(FlaskForm):
    title = TextField(validators=[DataRequired()])
    summary = TextAreaField()
    content = TextAreaField(validators=[DataRequired()])
    slug = TextField(validators=[DataRequired()])
    categories = SelectMultipleField()


class ModifyPostForm(FlaskForm):
    title = TextField(validators=[DataRequired()])
    summary = TextAreaField()
    content = TextAreaField(validators=[DataRequired()])
    slug = TextField(validators=[DataRequired()])
    categories = SelectMultipleField()


class CategoryForm(FlaskForm):
    name = TextField(validators=[DataRequired()])
    slug = TextField(validators=[DataRequired()])
    description = TextAreaField()

class ModifyCategoryForm(FlaskForm):
    name = TextField(validators=[DataRequired()])
    slug = TextField(validators=[DataRequired()])
    description = TextAreaField()