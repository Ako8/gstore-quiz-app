from app import app, db, Subject, Question, Answer


def populate_db():
    with app.app_context():
        # Clear existing data
        db.drop_all()
        db.create_all()

        # Create subjects
        history = Subject(name="ისტორია", icon="book")
        science = Subject(name="ქიმია", icon="flask")
        literature = Subject(name="ქართული ენა და ლიტერატურა", icon="feather")
        math = Subject(name="მათემატიკა", icon="calculator")

        db.session.add_all([history, science, literature, math])
        db.session.commit()

        # Create questions and answers for History
        q1 = Question(text="Who was the first President of the United States?", subject=history, difficulty="medium")
        q1.answers = [
            Answer(text="George Washington", is_correct=True),
            Answer(text="Thomas Jefferson", is_correct=False),
            Answer(text="Abraham Lincoln", is_correct=False),
            Answer(text="John Adams", is_correct=False)
        ]

        q2 = Question(text="In which year did World War II end?", subject=history, difficulty="medium")
        q2.answers = [
            Answer(text="1943", is_correct=False),
            Answer(text="1945", is_correct=True),
            Answer(text="1947", is_correct=False),
            Answer(text="1950", is_correct=False)
        ]

        # Create questions and answers for Science
        q3 = Question(text="What is the chemical symbol for gold?", subject=history, difficulty="medium")
        q3.answers = [
            Answer(text="Au", is_correct=True),
            Answer(text="Ag", is_correct=False),
            Answer(text="Fe", is_correct=False),
            Answer(text="Cu", is_correct=False)
        ]

        q4 = Question(text="What is the largest planet in our solar system?", subject=history, difficulty="medium")
        q4.answers = [
            Answer(text="Earth", is_correct=False),
            Answer(text="Mars", is_correct=False),
            Answer(text="Jupiter", is_correct=True),
            Answer(text="Saturn", is_correct=False)
        ]

        # Create questions and answers for Literature
        q5 = Question(text="Who wrote 'Romeo and Juliet'?", subject=history, difficulty="medium")
        q5.answers = [
            Answer(text="Charles Dickens", is_correct=False),
            Answer(text="William Shakespeare", is_correct=True),
            Answer(text="Jane Austen", is_correct=False),
            Answer(text="Mark Twain", is_correct=False)
        ]

        q6 = Question(text="Which novel begins with the line 'It was the best of times, it was the worst of times'?",
                      subject=history, difficulty="medium")
        q6.answers = [
            Answer(text="Pride and Prejudice", is_correct=False),
            Answer(text="Great Expectations", is_correct=False),
            Answer(text="A Tale of Two Cities", is_correct=True),
            Answer(text="Moby-Dick", is_correct=False)
        ]

        q7 = Question(text="Which novel begins with the line 'It was the best of times, it was the worst of times'?",
                      subject=history, difficulty="medium")
        q7.answers = [
            Answer(text="Pride and Prejudice", is_correct=False),
            Answer(text="Great Expectations", is_correct=False),
            Answer(text="A Tale of Two Cities", is_correct=True),
            Answer(text="Moby-Dick", is_correct=False)
        ]

        q8 = Question(text="Which novel begins with the line 'It was the best of times, it was the worst of times'?",
                      subject=history, difficulty="medium")
        q8.answers = [
            Answer(text="Pride and Prejudice", is_correct=False),
            Answer(text="Great Expectations", is_correct=False),
            Answer(text="A Tale of Two Cities", is_correct=True),
            Answer(text="Moby-Dick", is_correct=False)
        ]

        db.session.add_all([q1, q2, q3, q4, q5, q6, q7, q8])
        db.session.commit()


if __name__ == '__main__':
    populate_db()
    print("Database populated successfully!")
