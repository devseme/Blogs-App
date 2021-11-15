from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField,SelectField
from wtforms.fields.simple import TextAreaField
from wtforms.validators import Required, Email, Length, EqualTo
from ..models import User,Blog
from wtforms import ValidationError



class BlogForm(FlaskForm):
    title = StringField('Blog title', validators=[Required()])
    category = SelectField('Blog category',choices=[('Select a category','Select a category'),('E News', 'E news'),('World Travel','World Travel'),('Photography','Photography'),('Entertainment','Entertainment')], validators=[Required()])
    content = TextAreaField('Body', validators=[Required()])
    created_by= StringField('Blog created_by',validators=[Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell Us About Yourself...',validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfileForm(FlaskForm):
    name = StringField('Name', validators=[Required(), Length(1, 64)])
    username = StringField('Username', validators=[Required(), Length(1, 64)])
    email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
    bio = TextAreaField('About...', validators=[Required(), Length(1, 100)])
    submit = SubmitField('Submit')   


class CommentForm(FlaskForm):
    comment = TextAreaField('Body', validators=[Required()])
    submit = SubmitField('Submit')

