from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///license.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Fullname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    license_plate = db.Column(db.String(10), unique=True,  nullable=False)
    number = db.Column(db.String(15), nullable=False)
    
    
    def __repr__(self):
        return f"User('{self.Fullname}') with license plate ('{self.license_plate}')"
        

@app.route('/modal')
def index():
        return render_template('modal.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',)


