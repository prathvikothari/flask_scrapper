from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def get_beer():
    r = requests.get('https://api.punkapi.com/v2/beers/random')
    beer_json = r.json()
    name = beer_json[0]['name']
    abv = beer_json[0]['abv']
    description = beer_json[0]['description']
    food_pairing = beer_json[0]['food_pairing']

    beer = {
        'name' : name,
        'abv' : abv,
        'description' : description,
        'foodpair' : food_pairing
    }

    print(beer)

    return render_template('index.html', beer = beer)