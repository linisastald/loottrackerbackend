# app.py

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://plt:alltheloot@localhost:5432/pathfinder_loot_tracker'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import models


@app.route('/campaign', methods=['GET'])
def get_campaigns():
    campaigns = models.Campaign.query.all()
    return {"campaigns": [campaign.serialize() for campaign in campaigns]}


if __name__ == '__main__':
    app.run(debug=True)
