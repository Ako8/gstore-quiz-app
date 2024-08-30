from app import app, db, Subject, Question, Answer


def populate_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        history = Subject(name="ისტორია", icon="book")
        math = Subject(name="მათემატიკა", icon="calculator")
        literature = Subject(name="ქართული ენა და ლიტერატურა", icon="feather")
        science = Subject(name="სახალისო", icon="laugh-squint")

        db.session.add_all([history,  math, literature, science])
        db.session.commit()


if __name__ == '__main__':
    populate_db()
    print("Database populated successfully!")
