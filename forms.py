from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField, SelectField, StringField
from wtforms.validators import DataRequired

class TranslationForm(FlaskForm):
    text_to_translate = StringField('Text to Translate', validators=[DataRequired()])
    target_language = SelectField('Target Language', choices=[('en', 'English'), ('de', 'German'), ('es', 'Spanish')], validators=[DataRequired()])
    text_to_speech_language = SelectField('Text-to-Speech Language', choices=[('en', 'English'), ('de', 'German'), ('es', 'Spanish')], validators=[DataRequired()])
    submit = SubmitField('Translate')

# Update forms.py
class SpeechToTextForm(FlaskForm):
    audio_data = TextAreaField('Audio Data')  # New field for capturing audio data
    submit = SubmitField('Convert to Text')


# Update forms.py
class TextTranslationForm(FlaskForm):
    text = TextAreaField('Enter Text', validators=[DataRequired()])
    language = SelectField('Select Language', choices=[
        ('en', 'English'),
        ('es', 'Spanish'),
        ('fr', 'French'),
        ('de', 'German'),
        ('zh-cn', 'Chinese Simplified'),  # Example: Chinese Simplified
        ('hi', 'Hindi'),                  # Example: Hindi
        ('ja', 'Japanese'),               # Example: Japanese
        ('ko', 'Korean')                  # Example: Korean
        # Add more languages as needed
    ], validators=[DataRequired()])
    submit = SubmitField('Translate')
