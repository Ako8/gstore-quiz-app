from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import uuid

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
db = SQLAlchemy(app)


class Subject(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    icon = db.Column(db.String(50), nullable=False)
    questions = db.relationship('Question', backref='subject', lazy=True)


class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(500), nullable=False)
    difficulty = db.Column(db.String(500), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id'), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)


class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(200), nullable=False)
    is_correct = db.Column(db.Boolean, nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)


@app.route('/9d18677d-ea9e-456e-b7d2-946a0da52abb')
def home():
    subjects = Subject.query.all()
    return render_template('home.html', subjects=subjects)


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


@app.route('/9d18677d-ea9e-456e-b7d2-946a0da52abb/result/<int:total_questions>', methods=['POST'])
def result(total_questions):
    print(total_questions)
    correct_answers = 0
    for key, value in request.form.items():
        if key.startswith('question_'):
            question_id = int(key.split('_')[1])
            selected_answer_id = int(value)
            correct_answer = Answer.query.filter_by(question_id=question_id, is_correct=True).first()
            if correct_answer.id == selected_answer_id:
                correct_answers += 1

    score_percentage = (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    return render_template('result.html', correct_answers=correct_answers, total_questions=total_questions,
                           score_percentage=score_percentage)


if __name__ == '__main__':
    app.run(debug=True)
