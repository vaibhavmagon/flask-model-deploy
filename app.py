from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Libraries for machine Learning.
import pickle
import pandas as pd


app = Flask(__name__)
# Database Connection
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)


# Models defined.
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    completed = db.Column(db.Integer, default=0)
    spam_check = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Todo %r>' % self.id


# Routes, Controllers & Services
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']  # Get data from content input
        new_task = Todo(content=task_content)  # Set to Model
        try:
            db.session.add(new_task)  # Added to DB
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error!'
    else:
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks=tasks)


@app.route('/delete/<int:id>')
def delete(id):
    task_delete = Todo.query.get_or_404(id)
    print(task_delete)
    try:
        db.session.delete(task_delete)  # Deleted from DB
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error!'


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content']  # Get data from content input
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error!'
    else:
        return render_template('update.html', task=task)


@app.route('/spamCheck/<int:id>')
def spamCheck(id):
    task = Todo.query.get_or_404(id)
    taskPd = pd.DataFrame({'sms': [task.content]})
    count_vector = pickle.load(open('vector.pkl', 'rb'))
    testing_data = count_vector.transform(taskPd.iloc[:, 0])
    model = pickle.load(open('spam_model.sav', 'rb'))  # Load SPAM HAM Model.
    y_score = model.predict(testing_data)
    print(y_score)
    if y_score[0] == 1:
        print('Spam')
        task.spam_check = 1
    else:
        print('Not Spam')
        task.spam_check = 2

    try:
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an error!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000', debug=True)
