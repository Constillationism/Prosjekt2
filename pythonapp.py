from flask import Flask
import mariadb

app = Flask(__name__)

@app.route('/')
def():

mariadb = mariadb.connect

def søkemotor():
    klientsøk = input("Søk etter produkter")
    print("Table")

søkemotor()

