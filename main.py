from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from clpr import get_license_plates

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super_secretive_key'
app.config['UPLOAD_FOLDER'] = 'static/files'

class UploadFileForm(FlaskForm):
    file = FileField("File")
    submit = SubmitField("Get Plates")

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        res = get_license_plates(str(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename))))
        show_this = ""
        for plate in res:
            show_this += "License: " + plate[0] + ", Time: " + plate[1] + "\n"
        return show_this
    return render_template('index.html', form=form)

if __name__=='__main__':
    app.run(debug=True)
