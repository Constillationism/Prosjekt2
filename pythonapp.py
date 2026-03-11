from flask import Flask
import mariadb

mariadb = mariadb.connect

def søkemotor():
    klientsøk = input("Søk etter produkter")
    print("Table")

søkemotor()

