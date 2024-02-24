from flask import Flask, request, send_file
from PIL import Image
from io import BytesIO

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    # Send the static file named 'index.html' as the response
    return app.send_static_file('index.html')

# Route for compressing images
@app.route('/compress', methods=['POST'])
def compress():
    # Get the image file from the request
    image = request.files['image']
    # Open the image using PIL
    picture = Image.open(image)
    # Create a BytesIO object to store the compressed image
    img_io = BytesIO()
    # Save the image to the BytesIO object as a JPEG with optimization and specified quality
    picture.save(img_io, 'JPEG', optimize=True, quality=30)
    # Seek to the beginning of the BytesIO object
    img_io.seek(0)
    # Return the compressed image file as a response
    return send_file(img_io, mimetype='image/jpeg', as_attachment=True, download_name='compressed.jpg')

# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run()

