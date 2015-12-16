from flask import Flask 
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://scott:tiger@localhost/mydatabase'
db = SQLAlchemy(app)

class Example(db.Model):
	__tablename__ = 'example'
	id = db.Column('id', db.Integer, primary_key=True)
	data = db.Column('data', db.Unicode)

	def __init__(self, id, data):
		self.id = id
		self.data = data