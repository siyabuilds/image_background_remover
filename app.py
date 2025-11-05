from flask import Flask, render_template, request, send_file
from rembg import remove
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
RESULT_FOLDER = 'static/results'

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove', methods=['POST'])
def remove_bg():
    if 'image' not in request.files:
        return "No file part", 400

    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400

    filename = secure_filename(file.filename)
    input_path = os.path.join(UPLOAD_FOLDER, filename)
    output_path = os.path.join(RESULT_FOLDER, f'removed_{filename}')
    file.save(input_path)

    # read input bytes, run rembg.remove (returns bytes), write output
    with open(input_path, "rb") as inp:
        input_bytes = inp.read()

    try:
        output_bytes = remove(input_bytes)
    except Exception as e:
        return f"Background removal failed: {e}", 500

    with open(output_path, "wb") as out:
        out.write(output_bytes)

    return send_file(output_path, mimetype='image/png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)