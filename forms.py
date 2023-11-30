from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DateTimeField
from wtforms.validators import DataRequired

class AktualitaForm(FlaskForm):
    titulek = StringField('Titulek', validators=[DataRequired()])
    obsah = TextAreaField('Obsah', validators=[DataRequired()])
    # Použijeme DateTimeField místo DateTimeLocalField
    datum_publikace = DateTimeField('Datum a čas publikace', format='%Y-%m-%d %H:%M', validators=[DataRequired()])
    submit = SubmitField('Odeslat')
