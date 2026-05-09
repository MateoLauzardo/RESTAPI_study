from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy 


app = Flask(__name__)



# ------------ EVERYTHING BETWEEN IS TO create data base and routes ------------


# create a database 'sqlite:///travel.db' <- "travel" can be anything
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///travel.db'

# the connection tool for database / db just gives you the methods to interact with the database 
db = SQLAlchemy(app)


# (PYTHON USING RAW SQL) create a model for the database -> has columns and data types
class Destination(db.Model):
    id = db.Column(db.Integer, primary_key=True) 
    destination = db.Column(db.String(50), nullable=False)
    country = db.Column(db.String(50), nullable=False)
    rating = db.Column(db.Float(2, 1), nullable=False)

    
    # method to convert model to a dictionary / JSON format (what API will return)
    # method lives inside the class because it belongs to that data 
    def to_dict(self):
        return {
            'id': self.id,
            'destination': self.destination,
            'country': self.country,
            'rating': self.rating
        }

# Turn the tables on when the app starts
with app.app_context():
    db.create_all() 




@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Travel API!"})




# route to get all destinations from the database and return them as JSON
@app.route('/destinations', methods=['GET'])
def get_destinations():
    destinations = Destination.query.all()
    return jsonify([destination.to_dict() for destination in destinations])
    
    
    

# route to get a specific destination by ID from the database and return it as JSON
@app.route('/destinations/<int:destination_id>', methods=['GET'])
def get_destination(destination_id):
    destination = Destination.query.get(destination_id)
    if destination:
        return jsonify(destination.to_dict())
    else:
        return jsonify({"error": "Destination not found"}), 404
    
    
    
# route to add a new destination to the database using POST request with JSON data
@app.route('/destinations', methods=['POST'])
def add_destination():
    data = request.get_json()
    
    new_destination = Destination(
        destination=data['destination'],
        country=data['country'],
        rating=data['rating']
    )
    
    
    # add the new destination to the database and commit the changes
    db.session.add(new_destination)
    db.session.commit()
    
    return jsonify(new_destination.to_dict()), 201



# route to update an existing destination in the database using PUT request with JSON data
@app.route('/destinations/<int:destination_id>', methods=['PUT'])
def update_destination(destination_id):
    data = request.get_json()
    
    destination = Destination.query.get(destination_id)
    if destination:
        destination.destination = data.get('destination', destination.destination)
        destination.country = data.get('country', destination.country)
        destination.rating = data.get('rating', destination.rating)
        
        db.session.commit()
        
        return jsonify(destination.to_dict())

    else:
        return jsonify({"error": "Destination not found"}), 404
    


# route to delete a destination from the database using DELETE request
@app.route('/destinations/<int:destination_id>', methods=['DELETE'])
def delete_destination(destination_id):
    
    destination = Destination.query.get(destination_id)
    if destination:
        db.session.delete(destination)
        db.session.commit()
        return jsonify({"message": "Destination deleted successfully"})
    else:
        return jsonify({"error": "Destination not found"}), 404
    
# -----------------------------------------------------------------------------------



# just starts the server
if __name__ == '__main__':
    app.run(debug=True)
