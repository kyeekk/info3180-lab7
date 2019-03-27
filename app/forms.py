from flask_wtf import FlaskForm
from wtforms import Form, TextAreaField, SubmitField
from wtforms.validators import DataRequired, InputRequired, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

class UploadForm(FlaskForm):
    description = TextAreaField('Descriptioon', validators=[
        InputRequired(),
        Length(min=15, max=200, message="Can enter from 15 to 200 characters.")
    ])
    photo = FileField('Image', validators=[
        FileRequired("You need a profile pic."), 
        FileAllowed(['jpg','png'], 'Images only!')
    ])
    submit = SubmitField("Add Profile")
