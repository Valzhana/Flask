from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase_books.db'
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    year = db.Column(db.String(120), nullable=False)
    count = db.Column(db.String(10), nullable=False)
    id_author = db.Column(db.Integer, db.ForeignKey('author.id'))
    authors = db.relationship('Author', secondary='book_author', backref='books', lazy=True)

    def __repr__(self):
        return f'{self.name} {self.year} {self.count}'


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'{self.firstname} {self.lastname}'


class BookAuthor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

    def __repr__(self):
        return f'{self.name}'
