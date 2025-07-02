from flask import Flask, render_template, request, redirect, url_for
import os
from PIL import Image
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['PROCESSED_FOLDER'] = 'static/processed'
# Create folders if they don't exist
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['PROCESSED_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST':
        if 'image' not in request.files:
            return "No image part"
        file = request.files['image']
        if file.filename == '':
            return "No selected file"
        if file:
            filename = f"{uuid.uuid4().hex}.png"
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Convert to black and white
            img = Image.open(filepath).convert('L')  # 'L' mode = grayscale
            processed_path = os.path.join(app.config['PROCESSED_FOLDER'], filename)
            img.save(processed_path)

            return render_template('index.html', 
                                   original_image='uploads/' + filename,
                                    processed_image='processed/' + filename
                                    )

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=False)
