from flask import Flask, request, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Route for serving the index.html file
@app.route('/')
def index():
    return app.send_static_file('index.html')

# Route for handling image compression
@app.route('/compress', methods=['POST'])
def compress():
    # Get the image file from the request
    image = request.files['image']
    
    # Open the image using PIL
    picture = Image.open(image)
    
    # Create a BytesIO object to hold the compressed image
    img_io = BytesIO()
    
    # Compress the image and save it to the BytesIO object
    picture.save(img_io, 'JPEG', optimize=True, quality=30)
    
    # Reset the file pointer of the BytesIO object to the beginning
    img_io.seek(0)
    
    # Send the compressed image file back to the client as an attachment
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')

if __name__ == '__main__':
    app.run()

