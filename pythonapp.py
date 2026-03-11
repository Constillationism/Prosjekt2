from flask import Flask
import mariadb

mariadb = mariadb.connect(
    import db.sql
)

def søkemotor():
    klientsøk = input("Søk etter produkter"):


