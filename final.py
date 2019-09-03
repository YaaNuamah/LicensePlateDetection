import os
import urllib.request
from openalpr import core
from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
from flask_sqlalchemy import SQLAlchemy
from hubtel import sms

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

UPLOAD_FOLDER = '/static/uploads/'

app = Flask(__name__)
app.secret_key = "secret key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///license.db'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Fullname = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    license_plate = db.Column(db.String(10), unique=True,  nullable=False)
    number = db.Column(db.String(15), nullable=False)
    
    
    def __repr__(self):
        return f"User('{self.Fullname}') with license plate ('{self.license_plate}') and number ('{self.number}')"

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/home/')
def upload_form():
    return render_template('homepage.html')
                        

@app.route('/message', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename))
            name = os.path.join(os.getcwd() + UPLOAD_FOLDER, file.filename)
            extracted_text = core(str(name))
            plate = User.query.filter_by(license_plate=extracted_text).all()
            if plate == '':
                negative = 'No such person matches the license plate uploaded'
            else:
                results = plate
            flash('File successfully uploaded')
            return render_template('finalpage.html', msg='Successfully processed', results=results, negative='No such person matches the license plate uploaded')
        else:
            flash('Allowed file types are .....')
            return redirect(request.url)


@app.route('/success', methods=['POST'])
def get_file():
    if request.method == 'POST':
        tel = request.form.get('number')
        option = request.form.get('option')
        message = request.form.get('message')
        if option != '' and message == '':
            sms(str(tel), str(option))
        elif option != '' and message != '':
            sms(str(tel), str(option + '. ' + message))
        elif option == '' and message != '':
            sms(str(tel), str(message))
            
        return render_template('homepage.html', string='Message sent!')
    else:
            return redirect(request.url)
    

            
            
        
if __name__ == '__main__':
    app.run()
            
