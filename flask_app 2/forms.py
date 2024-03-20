from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from werkzeug.utils import secure_filename
from wtforms import StringField, IntegerField, SubmitField, TextAreaField, PasswordField, SelectField
from wtforms.validators import (
    InputRequired,
    DataRequired,
    NumberRange,
    Length,
    Email,
    EqualTo,
    ValidationError,
)


from .models import User


class SearchForm(FlaskForm):
    search_query = StringField(
        "Query", validators=[InputRequired(), Length(min=1, max=100)]
    )
    submit = SubmitField("Search")
    
class RestaurantReviewForm(FlaskForm):
    comment = TextAreaField(
        "Comment", validators=[InputRequired(), Length(min=5, max=500)]
    )
    image = FileField("Image", validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])
    rating = SelectField('Rating', choices=[(1,"★☆☆☆☆"),(2,"★★☆☆☆"),(3,"★★★☆☆"),(4,"★★★★☆"),(5,"★★★★★")])
    
    submit = SubmitField("Post")
    
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[InputRequired(), Length(min=1, max=40)]
    )
    email = StringField("Email", validators=[InputRequired(), Email()])
    password = PasswordField("Password", validators=[InputRequired()])
    confirm_password = PasswordField(
        "Confirm Password", validators=[InputRequired(), EqualTo('password', 'Passwords do not match')]
    )
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.objects(username=username.data).first()
        if user is not None:
            raise ValidationError("Username is taken")

    def validate_email(self, email):
        user = User.objects(email=email.data).first()
        if user is not None:
            raise ValidationError("Email is taken")
        
    def validate_password(self, password):
        p = password.data
        if len(p) < 8:
            raise ValidationError('Password must be at least 8 characters.')
        if not any(char.isdigit() for char in p):
            raise ValidationError('Password must contain at least one digit.')
        elif not any(char.isalpha() for char in p):
            raise ValidationError('Password must contain at least one letter.')
        elif not any(not char.isalnum() for char in p):
            raise ValidationError('Password must contain at least one special character')
            
            
        
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired(), Length(min=1, max=40)])
    password = PasswordField("Password", validators=[InputRequired()])
    submit = SubmitField("Log In")

class UpdateFoodForm(FlaskForm):
    food = StringField(
        "Food", validators=[InputRequired(), Length(min=1, max=40)]
    )
    submit = SubmitField("Update")

class UpdateProfilePicForm(FlaskForm):
    profile_picture = FileField("Profile Picture", validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Images Only!')])
    submit = SubmitField("Update")

