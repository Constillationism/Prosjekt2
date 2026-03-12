from flask import Flask
import mariadb

mariadb = mariadb.connect
app = Flask(__name__)

@app.route('/')
def test():
    print(float(5))

def søkemotor():
    klientsøk = input("Søk etter produkter")
    print("Table")

søkemotor()

