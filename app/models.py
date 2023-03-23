from app import db

class Input(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(140))
    time = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Input {self.id}>'
