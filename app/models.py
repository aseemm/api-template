from app import db
from app import app

class Book(db.Model):
    __searchable__ = ['title']
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(256))
    author = db.Column(db.String(256))
    link = db.Column(db.Text)

    def __repr__(self):  # pragma: no cover
        return '<Book %r>' % (self.title)
