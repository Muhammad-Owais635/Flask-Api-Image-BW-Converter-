
# 📸 Image BW Converter (Flask App)

A lightweight Flask-based web application that allows users to upload an image, converts it to black and white (grayscale), and displays both the original and processed images.

---

## 🚀 Features

- Upload images via a simple web interface
- Convert images to black & white using Pillow
- View original and processed images side by side
- Images stored in `static/uploads` and `static/processed`
- Auto-creates necessary folders if missing

---

## 🛠️ Requirements

- Python 3.x
- Flask
- Pillow (PIL fork)

---

## 📦 Installation

```bash
# Clone the repository
git clone https://github.com/your-username/image-bw-converter.git
cd image-bw-converter

# (Optional) Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```

---

## 📁 Project Structure

```
image-bw-converter/
├── app.py
├── static/
│   ├── uploads/
│   └── processed/
├── templates/
│   └── index.html
└── requirements.txt
```

> Note: `uploads/` and `processed/` folders are created automatically by the app.

---

## 🖼️ Usage

1. Start the app:  
   ```bash
   python app.py
   ```
2. Open your browser and visit `http://localhost:5000`
3. Upload an image (PNG, JPG, etc.)
4. The app will show both the original and black & white versions

---

## ✅ requirements.txt

```txt
Flask
Pillow
```

---

## 📤 Deployment

- Localhost for testing: `python app.py`
- For production, consider using:
  - Gunicorn with Nginx
  - Heroku or Render
  - Docker

---

## 📝 License

This project is licensed under the MIT License.

---

## 🧠 Suggested GitHub Repo Names

- `image-bw-converter`
- `flask-bw-image-processor`
- `flask-image-grayscale`
- `bwify`
