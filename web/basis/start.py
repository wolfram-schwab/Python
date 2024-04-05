from flask import Flask
from flask import render_template
#  from flask import request


app = Flask(__name__, template_folder='templates/kurs')
app.secret_key = 'D!mPbFs2022'


# Lies die Konfiguration der aktuellen Anwnendung
# und registriere Blueprints (Module, Kapitel)
from pathlib import Path
import sys

themenpfad = Path.cwd().parent / 'themen'
dbpfad = Path.cwd().parent / 'datenbanken'

sys.path.insert(0, str(dbpfad))
sys.path.insert(0, str(themenpfad))


import configparser as cnf
import importlib
import collections as col

parser = cnf.ConfigParser()
parser.read('static/data/ini/web.ini', encoding='utf8')

themen = col.OrderedDict()
importe = parser['Import']
for kapitel in importe :
    paket  = f"{kapitel}.{kapitel}"
    print(paket)
    modul = importlib.import_module(paket)
    app.register_blueprint(modul.blueprint(), url_prefix=f'/{kapitel}')
    themen[kapitel] = importe[kapitel].capitalize()

aufgaben = parser['Aufgaben']

# print("Themen", themen)

from static import diagnose

@app.route('/')
@app.route('/index.html')
def index():
    list_format = "<li><a href='/{}'>{}</a></li>"
    return render_template('kurs_index.html'
                           ,themen=themen
                           ,list_format=list_format
                           ,aufgaben=aufgaben)

@app.route('/includes/<included>')
def einbeziehen(included=None):
    return render_template(f'/includes/{included}')

@app.route('/d_i_a_')
def dia() :
    return render_template('diagnose.html'
                          , cwd=Path.cwd()
                          , base=diagnose.base_dir())
@app.route('/__sitemap')
def site() :
    files = diagnose.filesystem()

    return render_template('sitemap.html',
                           directory = files)
                           
