from flask import Flask, request, render_template, send_file
import os
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

app = Flask(__name__)

if not os.path.exists("uploads"):
    os.makedirs("uploads")

@app.route('/', methods =["GET", "POST"])
def home():
    if request.method == "POST":
        image = request.files['image']
        upperText = request.form.get('ut')
        bottomText = request.form.get('bt')

        imageLocation = os.path.join("uploads", image.filename)
        image.save(imageLocation)

        imageToEdit = Image.open(imageLocation)
        width, height = imageToEdit.size
        d = ImageDraw.Draw(imageToEdit)
        fontSize = 50
        f = ImageFont.truetype("arial.ttf",fontSize)

        _, _, w, _= d.textbbox((0, 0), upperText, font=f)
        d.text(((width-w)/2, fontSize+20), upperText, font=f, fill="white")
        _, _, w, _= d.textbbox((0, 0), bottomText, font=f)
        d.text(((width-w)/2, height-fontSize-40), bottomText, font=f, fill = "white")

        imgIO = BytesIO()
        imageToEdit = imageToEdit.convert('RGB')
        imageToEdit.save(imgIO, 'JPEG', quality=70)
        imgIO.seek(0)
        return send_file(imgIO, mimetype='image/jpeg')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port = 5000)