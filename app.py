"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret-key'

connect_db(app)

@app.route("/cupcakes")
def list_all_cupcakes():
    """Return all cupcakes"""
    
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(all_cupcakes)