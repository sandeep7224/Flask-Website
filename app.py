from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, FileField, SelectField
from wtforms.validators import DataRequired
import speech_recognition as sr
from gtts import gTTS
import base64
from io import BytesIO
from googletrans import Translator

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class TextToSpeechForm(FlaskForm):
    text = TextAreaField('Enter Text', validators=[DataRequired()])
    submit = SubmitField('Convert to Speech')

class SpeechToTextForm(FlaskForm):
    audio = FileField('Upload Audio File', validators=[DataRequired()])
    submit = SubmitField('Convert to Text')

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

@app.route('/', methods=['GET', 'POST'])
def index():
    tts_form = TextToSpeechForm()
    stt_form = SpeechToTextForm()
    translation_form = TextTranslationForm()

    audio_data = None
    transcript = None
    translated_text = None
    tts_error = None
    stt_error = None
    translation_error = None

    if tts_form.validate_on_submit() and 'tts_form' in request.form:
        text = tts_form.text.data
        tts = gTTS(text=text, lang='en')
        mp3_fp = BytesIO()
        tts.write_to_fp(mp3_fp)
        mp3_fp.seek(0)
        audio_data = base64.b64encode(mp3_fp.read()).decode('utf-8')
    elif stt_form.validate_on_submit() and 'stt_form' in request.form:
        audio_file = stt_form.audio.data
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            try:
                transcript = recognizer.recognize_google(audio)
            except sr.UnknownValueError:
                stt_error = "Could not understand audio"
            except sr.RequestError:
                stt_error = "Could not request results; check your network connection"
    elif translation_form.validate_on_submit() and 'translation_form' in request.form:
        text = translation_form.text.data
        language = translation_form.language.data
        translator = Translator()
        try:
            translated = translator.translate(text, dest=language)
            translated_text = translated.text
        except Exception as e:
            translation_error = f"Translation error: {str(e)}"

    return render_template('index.html', tts_form=tts_form, stt_form=stt_form, translation_form=translation_form,
                           audio_data=audio_data, transcript=transcript, translated_text=translated_text,
                           tts_error=tts_error, stt_error=stt_error, translation_error=translation_error)

if __name__ == '__main__':
    app.run(debug=True)
