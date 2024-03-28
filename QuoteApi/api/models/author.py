from api import db


class AuthorModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    # Один из вариантов решения для каскадного удаления, связанных с автором цитат.
    quotes = db.relationship(
        'QuoteModel', backref='author', lazy='dynamic', cascade='all, delete')

    def __init__(self, name):
        self.name = name
        