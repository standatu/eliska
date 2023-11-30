from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(basedir, 'db', 'databaze.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

app.secret_key = '1234'  # Doporučuje se použít silnější klíč a ukládat jej bezpečně

db = SQLAlchemy(app)

# Import modelů a formulářů
from models import Aktualita
from forms import AktualitaForm

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/o-nas')
def o_nas():
    return render_template('o_nas.html')

@app.route('/aktuality')
def aktuality():
    vsechny_aktuality = Aktualita.query.all()
    return render_template('aktuality.html', aktuality=vsechny_aktuality)

@app.route('/aktuality/form', methods=['GET', 'POST'])
@app.route('/aktuality/form/<int:id>', methods=['GET', 'POST'])
def aktuality_form(id=None):
    form = AktualitaForm(request.form)
    if request.method == 'POST' and form.validate():
        if id:
            aktualita = Aktualita.query.get(id)
            if aktualita:
                form.populate_obj(aktualita)
        else:
            nova_aktualita = Aktualita()
            form.populate_obj(nova_aktualita)
            db.session.add(nova_aktualita)
        db.session.commit()
        return redirect(url_for('aktuality'))
    elif request.method == 'GET' and id:
        aktualita = Aktualita.query.get_or_404(id)
        form = AktualitaForm(obj=aktualita)
    
    return render_template('aktuality_form.html', form=form)

@app.route('/informace')
def informace():
    return render_template('informace.html')

@app.route('/dokumenty')
def dokumenty():
    return render_template('dokumenty.html')

@app.route('/kontakty')
def kontakty():
    return render_template('kontakty.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  
    app.run(debug=True)
