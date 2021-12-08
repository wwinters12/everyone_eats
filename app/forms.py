from flask_wtf import FlaskForm
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms import StringField, PasswordField, BooleanField, SubmitField, \
    TextAreaField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, \
    Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class EmptyForm(FlaskForm):
    submit = SubmitField('Submit')


class DishForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    rating = SelectField('Rating', coerce=int, choices=[0, 1, 2, 3, 4, 5], validators=[DataRequired()])
    price = IntegerField('Price', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Dish')


class RestaurantForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    rating = SelectField('Rating', coerce=int, choices=[0, 1, 2, 3, 4, 5], validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    submit = SubmitField('Add Restaurant')

class EditProfileForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    about_me = TextAreaField('About me', validators=[Length(min=0, max=140)])
    submit = SubmitField('Submit')

    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Please use a different username.')


class RestaurantReviewForm(FlaskForm):
    restaurantID = SelectField('Restaurant', coerce=int, choices=[])
    rating = SelectField('Rating', coerce=int, choices=[0, 1, 2, 3, 4, 5], validators=[DataRequired()])
    body = TextAreaField('Leave a Review', validators=[DataRequired()])
    submit = SubmitField('Submit')


class DishReviewForm(FlaskForm):
    dishID = SelectField('Dish', coerce=int, choices=[])
    rating = SelectField('Rating', coerce=int, choices=[0, 1, 2, 3, 4, 5], validators=[DataRequired()])
    body = TextAreaField('Leave a Review', validators=[DataRequired()])
    submit = SubmitField('Submit')

