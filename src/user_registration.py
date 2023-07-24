```python
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/uber_clone'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50), unique=True)
    phone = db.Column(db.String(20), unique=True)
    password = db.Column(db.String(80))

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'phone')

user_schema = UserSchema()
users_schema = UserSchema(many=True)

@app.route('/signup', methods=['POST'])
def registerUser():
    name = request.json['name']
    email = request.json['email']
    phone = request.json['phone']
    password = request.json['password']
    hashed_password = generate_password_hash(password, method='sha256')

    new_user = User(name, email, phone, hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return user_schema.jsonify(new_user)

@app.route('/users', methods=['GET'])
def getUsers():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```