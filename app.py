from flask import Flask, render_template, request, redirect
import os
import pandas as pd
from process_csv import transform_csv_to_txt
from ml_model import process_startup_descriptions

app = Flask(__name__)

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/data', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        
        if file:
            file.save(os.path.join('uploads', file.filename))

            csv_path = os.path.join('uploads', file.filename)
            txt_file_path = transform_csv_to_txt(csv_path)

            data_file = './uploads/company_data.txt'
            
            results = process_startup_descriptions(data_file)

            return render_template('data.html', results=results)

    return 'Upload failed'

if __name__ == '__main__':
    app.run(debug=True)
