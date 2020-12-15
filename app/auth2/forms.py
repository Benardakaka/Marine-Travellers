from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo,ValidationError
from ..models import Rider
from wtforms import StringField,PasswordField,BooleanField,SubmitField,IntegerField

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    ridername = StringField('Enter your name',validators = [Required()])
    number_plate = StringField('Enter your motorbike registration number (number plate)',validators = [Required()])
    motorbike_model= StringField('Enter your motorbike model',validators = [Required()])
    mobile_number = IntegerField('Enter your Mobile number',validators = [Required()])
    password = PasswordField('Password',validators = [Required(), EqualTo('password_confirm',message = 'Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators = [Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if Rider.query.filter_by(email =data_field.data).first():
            raise ValidationError('Sorry! There is an account with that email')

    def validate_ridername(self,data_field):
        if Rider.query.filter_by(ridername = data_field.data).first():
            raise ValidationError('Sorry!That ridername is already taken')


        
class LoginForm(FlaskForm):
    ridername = StringField('Ridername',validators=[Required()])
    email = StringField('Your Email Address',validators=[Required(),Email()])
    password = PasswordField('Password',validators =[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')
