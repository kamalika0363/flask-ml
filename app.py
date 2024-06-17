from flask import Flask, render_template, request, redirect
import os
from werkzeug.utils import secure_filename
from process_csv import transform_csv_to_txt
from ml_model import process_startup_descriptions

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def upload_form():
    return render_template('upload.html')

@app.route('/uploads', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'

        file = request.files['file']
        if file.filename == '':
            return 'No selected file'

        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            csv_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            txt_file_path = transform_csv_to_txt(csv_path)

            if txt_file_path:
                try:
                    with open(txt_file_path, 'r') as f:
                        lines = f.readlines()

                    print(f"Total lines read: {len(lines)}")
                    for line in lines:
                        print(line.strip())

                    for line in lines:
                        parts = line.strip().split(':')
                        if len(parts) >= 2:
                            key = parts[0].strip()
                            value = ':'.join(parts[1:]).strip()
                            
                    # file.save(os.path.join('uploads', file.filename))

                    # csv_path = os.path.join('uploads', file.filename)
                    # txt_file_path = transform_csv_to_txt(csv_path)

                    # data_file = './uploads/company_data.txt'
                    
                    process_startup_descriptions(txt_file_path)
                    
                except Exception as e:
                    return f'Error processing startup descriptions: {str(e)}'
                
            else:
                return 'Failed to transform CSV to TXT format'


    return 'Upload failed'


if __name__ == '__main__':
    app.run(debug=True)
