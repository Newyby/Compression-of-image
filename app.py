from flask import Flask, request, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/compress', methods=['POST'])
def compress():
    image = request.files['image']
    picture = Image.open(image)
    img_io = BytesIO()
    picture.save(img_io, 'JPEG', optimize=True, quality=30)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')

if __name__ == '__main__':
    app.run()
