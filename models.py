from app import db


class Dessert(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    MobileNumber = db.Column(db.Integer())
    email = db.Column(db.String(30))
    Subject = db.Column(db.String(100))
    sex = db.Column(db.String(10))

    def __init__(self, name, MobileNumber, email, Subject, sex):
        self.name = name
        self.MobileNumber = MobileNumber
        self.email = email
        self.Subject = Subject
        self.sex = sex


class Menu(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))

    def __init__(self, name, id):
        self.name = name
        self.id = id


def create_dessert(name, MobileNumber, email, Subject, sex):

    dessert = Dessert(name, MobileNumber, email, Subject, sex)

    db.session.add(dessert)

    db.session.commit()

    return dessert


if __name__ == "__main__":

    print("Creating database tables...")
    db.create_all()
    print("Done!")
