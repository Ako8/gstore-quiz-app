from app import app, db, Subject, Question, Answer


def populate_db():
    with app.app_context():
        db.drop_all()
        db.create_all()

        history = Subject(name="ისტორია", icon="book")
        math = Subject(name="მათემატიკა", icon="calculator")
        literature = Subject(name="ქართული ენა და ლიტერატურა", icon="feather")
        science = Subject(name="სახალისო", icon="laugh-squint")

        db.session.add_all([history, math, literature, science])
        db.session.commit()

        q1 = Question(text="ჩამოთვლილთაგან რომელი ცნობილი ადამინაი ცხოვრობდა მე-8 საუკუნეში", subject=history,
                      difficulty="easy")
        q1.answers = [
            Answer(text="გ) აბო", is_correct=True),
            Answer(text="დ) ამბო", is_correct=False),
            Answer(text="ა) ბო", is_correct=False),
            Answer(text="ბე) ბო", is_correct=False)
        ]

        q2 = Question(text="რამდენი წიბო აქვს n-კუთხა პირამიდას?", subject=math, difficulty="medium")
        q2.answers = [
            Answer(text="n+3", is_correct=False),
            Answer(text="2n", is_correct=True),
            Answer(text="n+1", is_correct=False),
            Answer(text="2n-1", is_correct=False)
        ]

        # Create questions and answers for Science
        q3 = Question(text="პარალელოგრამის ორი კუთხის ჯამი 150°-ის ტოლია. რას უდრის პარალელოგრამის ბლაგვი კუთხე",
                      subject=math, difficulty="easy")
        q3.answers = [
            Answer(text="105°", is_correct=False),
            Answer(text="110°", is_correct=True),
            Answer(text="115°", is_correct=False),
            Answer(text="120°", is_correct=False)
        ]

        q4 = Question(text="საბოლოოდ რომელ კუნძულზე გადაასახლეს ნაპოლეონი?", subject=history, difficulty="medium")
        q4.answers = [
            Answer(text="კუნძულ ელბაზე", is_correct=False),
            Answer(text="კუნძულ კორსიკაზე", is_correct=False),
            Answer(text="წმ.ელენეს კუნძულზე", is_correct=True),
            Answer(text="კუნძულ სიცილიაზე", is_correct=False)
        ]

        # Create questions and answers for Literature
        q5 = Question(text="რომელ წელს დაარსდა ჯისთორი", subject=history, difficulty="easy")
        q5.answers = [
            Answer(text="2020", is_correct=False),
            Answer(text="2022", is_correct=True),
            Answer(text="2004", is_correct=False),
            Answer(text="2021", is_correct=False)
        ]

        q6 = Question(text="სტრაბონის თანახმად, ვინ იყვნენ 'ლაოები' ქართლის სამეფოში",
                      subject=history, difficulty="hard")
        q6.answers = [
            Answer(text="სამეფო მონები", is_correct=True),
            Answer(text="გათავისუფლებული მონები", is_correct=False),
            Answer(text="წვრილი ვაჭრები", is_correct=False),
            Answer(text="მეფის მრჩევლები", is_correct=False)
        ]

        q7 = Question(text="გაიხსენეთ იაკობ ხუცესის 'შუშანიკის წამება'. რა არის ასტამი?",
                      subject=literature, difficulty="medium")
        q7.answers = [
            Answer(text="რკინის საჩხრეკი ჯოხი", is_correct=True),
            Answer(text="კანის დაავადება", is_correct=False),
            Answer(text="ქურთუკი, ტყავის მოსასხამი", is_correct=False),
            Answer(text="აბრეშუმის ხელსაქმე", is_correct=False)
        ]

        q8 = Question(text="რომელი მწკრივის ფორმა არ არის თხრობითი კილოსი?",
                      subject=literature, difficulty="hard")
        q8.answers = [
            Answer(text="პირველი თურმეობითი", is_correct=False),
            Answer(text="უწყვეტელი", is_correct=False),
            Answer(text="ხოლმეობითი", is_correct=False),
            Answer(text="მეორე კავშირებითი", is_correct=True)
        ]

        q9 = Question(
            text="გაიხსენეთ ჯემალ ქარჩხაძის 'იგი'. რა მოიხსენიება ნაწარმოებში შემდეგი სიტქვებით: 'ცის დღის თვალი'",
            subject=literature, difficulty="easy")
        q9.answers = [
            Answer(text="იგი", is_correct=False),
            Answer(text="მზე", is_correct=True),
            Answer(text="ვარსკვლავები", is_correct=False),
            Answer(text="მთვარე", is_correct=False)
        ]

        q10 = Question(
            text="ორმა მორბენალმა წრიული ფორმის სარბენი ბილიკის ერთი და იმავე ადგილიდან ურთიერთსაწინააღმდეგო "
                 "მიმართულებით მუდმივი სიჩქარეებით ერთდროულად დაიწყო სირბილი და პირველად ერთმანეთს 6 წუთის შემდეგ "
                 "შეხვდნენ. იმავე სიჩქარეებით სირბილისას პირველი მორბენალი 5 წუთით უფრო ჩქარა შემოურბენს სარბენ "
                 "ბილიკს, ვიდრე მეორე მორბენალი. რამდენ წუთში შემოურბენს სარბენ ბილიკს პირველი მორბენალი?",
            subject=math, difficulty="hard")
        q10.answers = [
            Answer(text="8 წთ", is_correct=False),
            Answer(text="10 წთ", is_correct=True),
            Answer(text="12 წთ", is_correct=False),
            Answer(text="9 წთ", is_correct=False)
        ]

        db.session.add_all([q1, q2, q3, q4, q5, q6, q7, q8, q9, q10])
        db.session.commit()


if __name__ == '__main__':
    populate_db()
    print("Database populated successfully!")
