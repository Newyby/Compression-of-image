# Import necessary modules from Flask
from flask import Flask, request, send_file

# Import the Python Imaging Library (PIL) for image processing
from PIL import Image

# Import BytesIO for handling image data
from io import BytesIO

# Create a Flask application instance
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def index():
    # Serve the static HTML file 'index.html' from the 'static' directory
    return app.send_static_file('index.html')

# Define a route for compressing images via POST method
@app.route('/compress', methods=['POST'])
def compress():
    # Access the uploaded image file from the request
    image = request.files['image']
    
    # Open the image using PIL (Python Imaging Library)
    picture = Image.open(image)
    
    # Create a BytesIO object to store the compressed image
    img_io = BytesIO()
    
    # Compress and save the image to the BytesIO object in JPEG format
    picture.save(img_io, 'JPEG', optimize=True, quality=30)
    
    # Seek to the beginning of the BytesIO object
    img_io.seek(0)
    
    # Send the compressed image file as a response
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')

# Entry point to run the Flask application
if __name__ == '__main__':
    app.run()

