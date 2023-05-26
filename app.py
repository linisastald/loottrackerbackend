# app.py
import models
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://plt:alltheloot@localhost:5432/pathfinder_loot_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
CORS(app)




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


@app.route('/campaign', methods=['POST'])
def add_campaign():
    data = request.get_json()
    # Remove id if it's in the data, let DB handle it
    data.pop('id', None)

    new_campaign = models.Campaign(
        name=data.get('name'),
        ap=data.get('ap'),
        start_date=data.get('start_date')
    )
    db.session.add(new_campaign)
    db.session.commit()
    return {"id": new_campaign.id}, 201


@app.route('/appraisal', methods=['POST'])
def create_appraisal():
    data = request.json
    new_appraisal = models.Appraisal(**data)
    db.session.add(new_appraisal)
    db.session.commit()
    return jsonify({"appraisal": new_appraisal.serialize()}), 201


@app.route('/campaign_character', methods=['POST'])
def create_campaign_character():
    data = request.json
    new_campaign_character = models.CampaignCharacter(**data)
    db.session.add(new_campaign_character)
    db.session.commit()
    return jsonify({"campaign_character": new_campaign_character.serialize()}), 201


@app.route('/character', methods=['POST'])
def create_character():
    data = request.json
    new_character = models.Character(**data)
    db.session.add(new_character)
    db.session.commit()
    return jsonify({"character": new_character.serialize()}), 201


@app.route('/gold', methods=['POST'])
def create_gold():
    data = request.json
    new_gold = models.Gold(**data)
    db.session.add(new_gold)
    db.session.commit()
    return jsonify({"gold": new_gold.serialize()}), 201


@app.route('/item', methods=['POST'])
def create_item():
    data = request.json
    new_item = models.Item(**data)
    db.session.add(new_item)
    db.session.commit()
    return jsonify({"item": new_item.serialize()}), 201


@app.route('/itemref', methods=['POST'])
def create_itemref():
    data = request.json
    new_itemref = models.Itemref(**data)
    db.session.add(new_itemref)
    db.session.commit()
    return jsonify({"itemref": new_itemref.serialize()}), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
