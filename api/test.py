from flask import Flask, request, Response, render_template, jsonify
from peewee import *

# Initialize Flask app
app = Flask(__name__)

# Database connection
db = SqliteDatabase('your_database.db')

# Define the User model
class UserModel(Model):
    username = CharField(unique=True)
    email = CharField(unique=True)
    phone = CharField()
    city = CharField()
    address = CharField()
    image = CharField()
    password = CharField()

    class Meta:
        database = db

# Create tables
db.connect()
db.create_tables([UserModel])

@app.route('/create_user', methods=['POST'])
def create_user():
    data = request.json
    try:
        user = UserModel.get((UserModel.username == data['username']) | (UserModel.email == data['email']))
        return render_template("Templates/Users/Register.ejs", error="User Already Exist")
    except DoesNotExist:
        user = UserModel.create(
            username=data['username'],
            email=data['email'],
            phone=data['phone'],
            city=data['city'],
            address=data['address'],
            image=data['image'],
            password=data['password']
        )
        token = generate_token(user)
        return render_template("Templates/Users/Profile.ejs", user=user), 200, {'access_token': token}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    try:
        user = UserModel.get((UserModel.username == data['username']) | (UserModel.email == data['username']))
        if bcrypt.check_password_hash(user.password, data['password']):
            token = generate_token(user)
            return render_template("Templates/Users/Profile.ejs", user=user), 200, {'access_token': token}
        else:
            return render_template("Templates/Users/Login.ejs", error="Make Sure You Do Remember Your email or password")
    except DoesNotExist:
        return render_template("Templates/Users/Login.ejs", error="User With Credentials Doesn't Exist")

@app.route('/users', methods=['GET'])
def get_all_users():
    users = UserModel.select()
    return jsonify({"data": [user.__dict__['_data'] for user in users]}), 200

@app.route('/profile', methods=['GET'])
def get_profile():
    user_id = request.user._id  # Assuming you have a user object in request
    user = UserModel.get_by_id(user_id)
    return render_template("Templates/Users/Profile", user=user)

@app.route('/delete_user/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        user = UserModel.get_by_id(user_id)
        user.delete_instance()
        return jsonify({"data": "User Deleted Successfully"}), 200
    except DoesNotExist:
        return jsonify({"error": "User not found"}), 404

@app.route('/update_user', methods=['PUT'])
def update_user():
    data = request.json
    user_id = request.user._id  # Assuming you have a user object in request
    try:
        user = UserModel.get_by_id(user_id)
        for key, value in data.items():
            setattr(user, key, value)
        user.save()
        return jsonify({"msg": "Profile Updated Successfully"}), 200
    except DoesNotExist:
        return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
