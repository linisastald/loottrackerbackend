# models.py

from app import db


class Appraisal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    date = db.Column(db.Date)
    who = db.Column(db.String(120))
    believed_value = db.Column(db.Float)


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    ap = db.Column(db.String(120))
    start_date = db.Column(db.Date)


class CampaignCharacter(db.Model):
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(120))
    name = db.Column(db.String(120))
    birth = db.Column(db.Date)
    death = db.Column(db.Date)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))


class Gold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_date = db.Column(db.DateTime)
    transaction_type = db.Column(db.String(120))
    notes = db.Column(db.String(120))
    copper = db.Column(db.Integer)
    silver = db.Column(db.Integer)
    gold = db.Column(db.Integer)
    platinum = db.Column(db.Integer)


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_date = db.Column(db.Date)
    quantity = db.Column(db.Integer)
    name = db.Column(db.String(120))
    unidentified = db.Column(db.Boolean)
    masterwork = db.Column(db.Boolean)
    type = db.Column(db.String(120))
    size = db.Column(db.String(120))
    status = db.Column(db.String(120))
    location = db.Column(db.String(120))
    who = db.Column(db.String(120))
    sold = db.Column(db.Boolean)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))
    campaign_item = db.Column(db.Boolean)
    magic_level = db.Column(db.Integer)
    magic_spell = db.Column(db.String(120))
    cost = db.Column(db.Float)


class Itemref(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    real_value = db.Column(db.Float)
    type = db.Column(db.String(120))
