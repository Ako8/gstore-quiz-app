import os
import random

from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SECRET_KEY'] = '45drtcyghjtyd655dtygvhjgtyd6'

UPLOAD_FOLDER = 'static/question_images'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

db = SQLAlchemy(app)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    questions = db.relationship('Question', backref='subject', lazy=True, cascade="all, delete-orphan")


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    image_filename = db.Column(db.String(255))
    long_ass_text = db.Column(db.Text())
    answers = db.relationship('Answer', backref='question', lazy=True, cascade="all, delete-orphan")


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)


@app.route('/9d18677d-ea9e-456e-b7d2-946a0da52abb')
def home():
    subjects = Subject.query.all()
    return render_template('home.html', subjects=subjects)


@app.route('/9d18677d-ea9e-456e-b7d2-946a0da52abb/delete/<int:id>')
def qdelete(id):
    q = Question.query.get(id)
    db.session.delete(q)
    db.session.commit()
    return redirect(url_for('add_question'))


@app.route('/9d18677d-ea9e-456e-b7d2-946a0da52abb/quizlevel/<int:subject_id>/')
def quiz_level(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    return render_template('quizlevel.html', subject=subject)


@app.route('/9d18677d-ea9e-456e-b7d2-946a0da52abb/quiz/<int:subject_id>/<string:difficulty>')
def quiz(subject_id, difficulty):
    subject = Subject.query.get_or_404(subject_id)

    if difficulty == 'easy':
        questions = Question.query.filter(Question.difficulty == "easy", Question.subject_id == subject.id).all()
    elif difficulty == 'medium':
        questions = Question.query.filter(Question.difficulty == "medium", Question.subject_id == subject.id).all()
    elif difficulty == "hard":
        questions = Question.query.filter(Question.difficulty == "hard", Question.subject_id == subject.id).all()
    else:
        return redirect(url_for('home'))

    random.shuffle(questions)
    for question in questions:
        random.shuffle(question.answers)

    return render_template('quiz.html', subject=subject, questions=questions, difficulty=difficulty)


@app.route('/9d18677d-ea9e-456e-b7d2-946a0da52abb/result/<int:total_questions>/<string:saprizo>', methods=['POST'])
def result(total_questions, saprizo):
    answer = None
    question = None
    if saprizo == "300":
        for key, value in request.form.items():
            if key.startswith('text_answer_'):
                print(key)
                question_id = int(key.split('_')[2])
                print(question_id)
                question = Question.query.get(question_id)
                answer = request.form.get(f"text_answer_{question_id}")


    correct_answers = 0
    for key, value in request.form.items():
        if key.startswith('question_'):
            question_id = int(key.split('_')[1])
            selected_answer_id = int(value)
            correct_answer = Answer.query.filter_by(question_id=question_id, is_correct=True).first()
            if correct_answer.id == selected_answer_id:
                correct_answers += 1


    score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    return render_template('result.html',question=question, correct_answers=correct_answers, total_questions=total_questions,
                           score_percentage=score_percentage, saprizo=saprizo, answer=answer)


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/9d18677d-ea9e-456e-b7d2-946a0da52abb/add_question', methods=['GET', 'POST'])
def add_question():
    if request.method == 'POST':
        subject_id = request.form['subject']
        difficulty = request.form['difficulty']
        question_text = request.form['question_text']
        long_ass_text = request.form['long_ass_text']
        correct_answer_index = int(request.form['correct_answer'])

        # Handle image upload
        image_filename = None
        if 'question_image' in request.files:
            file = request.files['question_image']
            if file and file.filename != '' and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file_path = os.path.join(UPLOAD_FOLDER, filename)
                file.save(file_path)
                image_filename = filename

        # Create new question with image_filename
        new_question = Question(
            text=question_text,
            subject_id=subject_id,
            difficulty=difficulty,
            image_filename=image_filename,
            long_ass_text=long_ass_text
        )
        db.session.add(new_question)
        db.session.commit()

        # Add answers
        for i in range(4):
            answer_text = request.form[f'answer_{i}']
            print(answer_text)
            is_correct = (i == correct_answer_index)
            new_answer = Answer(text=answer_text, is_correct=is_correct, question_id=new_question.id)
            db.session.add(new_answer)

        db.session.commit()

        flash('კითხვა წარმატებით დაემატა!', 'success')
        return redirect(url_for('add_question'))

    subjects = Subject.query.all()
    return render_template('add_question.html', subjects=subjects)


if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

if __name__ == '__main__':
    app.run(debug=True)
