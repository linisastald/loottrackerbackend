# models.py

from app import db


class Appraisal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('item.id'))
    date = db.Column(db.Date)
    who = db.Column(db.String(120))
    believed_value = db.Column(db.Float)

    def serialize(self):
        return {
            'id': self.id,
            'item_id': self.item_id,
            'date': self.date.isoformat() if self.date else None,
            'who': self.who,
            'believed_value': self.believed_value
        }


class Campaign(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    ap = db.Column(db.String(120))
    start_date = db.Column(db.Date)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'ap': self.ap,
            'start_date': self.start_date.isoformat() if self.start_date else None
        }


class CampaignCharacter(db.Model):
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'), primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey('character.id'), primary_key=True)

    def serialize(self):
        return {
            'campaign_id': self.campaign_id,
            'character_id': self.character_id
        }


class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    player = db.Column(db.String(120))
    name = db.Column(db.String(120))
    birth = db.Column(db.Date)
    death = db.Column(db.Date)
    campaign_id = db.Column(db.Integer, db.ForeignKey('campaign.id'))

    def serialize(self):
        return {
            'id': self.id,
            'player': self.player,
            'name': self.name,
            'birth': self.birth.isoformat() if self.birth else None,
            'death': self.death.isoformat() if self.death else None,
            'campaign_id': self.campaign_id
        }


class Gold(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    session_date = db.Column(db.DateTime)
    transaction_type = db.Column(db.String(120))
    notes = db.Column(db.String(120))
    copper = db.Column(db.Integer)
    silver = db.Column(db.Integer)
    gold = db.Column(db.Integer)
    platinum = db.Column(db.Integer)

    def serialize(self):
        return {
            'id': self.id,
            'session_date': self.session_date.isoformat() if self.session_date else None,
            'transaction_type': self.transaction_type,
            'notes': self.notes,
            'copper': self.copper,
            'silver': self.silver,
            'gold': self.gold,
            'platinum': self.platinum
        }


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

    def serialize(self):
        return {
            'id': self.id,
            'session_date': self.session_date.isoformat() if self.session_date else None,
            'quantity': self.quantity,
            'name': self.name,
            'unidentified': self.unidentified,
            'masterwork': self.masterwork,
            'type': self.type,
            'size': self.size,
            'status': self.status,
            'location': self.location,
            'who': self.who,
            'sold': self.sold,
            'campaign_id': self.campaign_id,
            'campaign_item': self.campaign_item,
            'magic_level': self.magic_level,
            'magic_spell': self.magic_spell,
            'cost': self.cost
        }


class Itemref(db.Model):
    name = db.Column(db.String(120), primary_key=True)
    real_value = db.Column(db.Float)
    type = db.Column(db.String(120))

    def serialize(self):
        return {
            'name': self.name,
            'real_value': self.real_value,
            'type': self.type
        }
