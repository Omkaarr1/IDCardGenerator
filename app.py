from flask import Flask, request, send_from_directory, render_template, redirect, url_for
import os
import subprocess

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
PROCESSED_IMAGE = 'static/output.png'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get names
        name1 = request.form.get('name1')
        name2 = request.form.get('name2')
        name3 = request.form.get('name3')
        
        # Get image
        if 'image' not in request.files:
            return redirect(request.url)
        
        image_file = request.files['image']
        if image_file.filename == '':
            return redirect(request.url)
        
        # Save image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'uploaded_image.png')
        image_file.save(image_path)
        
        # Process image with two Python scripts
        subprocess.run(['python', 'process_image_1.py'])
        subprocess.run(['python', 'process_image_2.py', name1,name2,name3])
        
        return redirect(url_for('download_file'))
    
    return render_template('index.html')

@app.route('/download')
def download_file():
    return send_from_directory(directory='static', path='output_image.png', as_attachment=True)

if __name__ == '__main__':
    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)
    app.run(debug=True)
