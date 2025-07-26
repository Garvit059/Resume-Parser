# app.py
from flask import Flask, render_template, request
import os
from parser import parse_resume

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file = request.files['resume']
        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            result = parse_resume(filepath)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
