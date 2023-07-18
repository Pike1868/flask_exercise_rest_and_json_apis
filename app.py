"""Flask app for Cupcakes"""
from flask import Flask, request, jsonify, render_template
from models import db, connect_db, Cupcake

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'secret-key'

connect_db(app)

@app.route("/api/cupcakes")
def list_all_cupcakes():
    """Return all cupcakes"""
    
    all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
    
    return jsonify(all_cupcakes)

@app.route("/api/cupcakes/<int:id>")
def list_cupcake_details(id):
    """Get data about a single cupcake, respond with JSON"""
    cupcake = Cupcake.query.get_or_404(id)
     
    return jsonify(cupcake.serialize())

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """Create a cupcake with flavor, size, rating and image data from the body of the request. Respond with JSON like: {cupcake: {id, flavor,size, rating, image}}."""
    
    new_cupcake = Cupcake(flavor=request.json['flavor'], size=request.json['size'], rating=request.json['rating'], image=request.json['image'])
    
    db.session.add(new_cupcake)
    db.session.commit()
    
    return (jsonify(new_cupcake=new_cupcake.serialize()), 201)

@app.route("/snacks/<int:id>", methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    
    cupcake.flavor = request.json.get('flavor', cupcake.flavor)
    cupcake.size = request.json.get('size', cupcake.size)
    cupcake.rating = request.json.get('rating', cupcake.rating)
    cupcake.image = request.json.get('image', cupcake.image)
    
    db.session.commit()
    
    return (jsonify(cupcake=cupcake.serialize()))


@app.route("/snacks/<int:id>", methods=["DELETE"])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    
    db.session.delete(cupcake)
    
    return jsonify(message="Deleted")