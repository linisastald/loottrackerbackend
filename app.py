# app.py

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://plt:alltheloot@localhost:5432/pathfinder_loot_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models
from flask import jsonify


@app.route('/appraisal', methods=['GET'])
def get_appraisals():
    appraisals = models.Appraisal.query.all()
    return jsonify({"appraisals": [appraisal.serialize() for appraisal in appraisals]})


@app.route('/campaign_character', methods=['GET'])
def get_campaign_characters():
    campaign_characters = models.CampaignCharacter.query.all()
    return jsonify(
        {"campaign_characters": [campaign_character.serialize() for campaign_character in campaign_characters]})


@app.route('/character', methods=['GET'])
def get_characters():
    characters = models.Character.query.all()
    return jsonify({"characters": [character.serialize() for character in characters]})


@app.route('/gold', methods=['GET'])
def get_golds():
    golds = models.Gold.query.all()
    return jsonify({"golds": [gold.serialize() for gold in golds]})


@app.route('/item', methods=['GET'])
def get_items():
    items = models.Item.query.all()
    return jsonify({"items": [item.serialize() for item in items]})


@app.route('/itemref', methods=['GET'])
def get_itemrefs():
    itemrefs = models.Itemref.query.all()
    return jsonify({"itemrefs": [itemref.serialize() for itemref in itemrefs]})


if __name__ == '__main__':
    app.run(debug=True)
