# forms.py
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, SelectField
from wtforms.validators import DataRequired

class TextToSpeechForm(FlaskForm):
    text = TextAreaField('Enter Text', validators=[DataRequired()])
    submit = SubmitField('Convert to Speech')

class SpeechToTextForm(FlaskForm):
    submit = SubmitField('Start Recording')

class TextTranslationForm(FlaskForm):
    text = TextAreaField('Enter Text to Translate', validators=[DataRequired()])
    language = SelectField('Select Language', choices=[
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('zh-cn', 'Chinese Simplified'),
        ('hi', 'Hindi')
        # Add more languages as needed
    ], validators=[DataRequired()])
    submit = SubmitField('Translate Text')
