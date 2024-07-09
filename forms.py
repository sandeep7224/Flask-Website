from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField, SelectField, StringField
from wtforms.validators import DataRequired

class TextToSpeechForm(FlaskForm):
    text_to_translate = TextAreaField('Text to Translate', validators=[DataRequired()])
    text_to_speech_language = SelectField('Text-to-Speech Language', choices=[
        ('en', 'English'),
        ('de', 'German'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('zh-cn', 'Chinese Simplified'),
        ('hi', 'Hindi'),
        ('ta', 'Tamil'),
        ('te', 'Telugu'),
        ('kn', 'Kannada'),
        ('ml', 'Malayalam'),
        ('mr', 'Marathi'),
        ('bn', 'Bengali'),
        ('gu', 'Gujarati'),
        ('pa', 'Punjabi'),
        ('or', 'Odia'),
        ('as', 'Assamese'),
        ('ur', 'Urdu')
    ], validators=[DataRequired()])
    submit_tts = SubmitField('Convert to Speech')


class SpeechToTextForm(FlaskForm):
    audio_data = TextAreaField('Audio Data')  # New field for capturing audio data
    submit = SubmitField('Convert to Text')

class TextTranslationForm(FlaskForm):
    text = TextAreaField('Enter Text', validators=[DataRequired()])
    language = SelectField('Select Language', choices=[
        ('en', 'English'),
        ('de', 'German'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('zh-cn', 'Chinese Simplified'),
        ('hi', 'Hindi'),
        ('ta', 'Tamil'),
        ('te', 'Telugu'),
        ('kn', 'Kannada'),
        ('ml', 'Malayalam'),
        ('mr', 'Marathi'),
        ('bn', 'Bengali'),
        ('gu', 'Gujarati'),
        ('pa', 'Punjabi'),
        ('or', 'Odia'),
        ('as', 'Assamese'),
        ('ur', 'Urdu')
    ], validators=[DataRequired()])
    submit = SubmitField('Translate')
