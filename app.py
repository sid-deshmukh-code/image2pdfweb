from flask import Flask, render_template, request, redirect, url_for
import os
import pdfkit

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
PDF_FOLDER = 'static/pdfs/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PDF_FOLDER'] = PDF_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        return redirect(request.url)

    if file:
        # Save the uploaded image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(image_path)

        # Convert the image to PDF
        pdf_path = os.path.join(app.config['PDF_FOLDER'], f'{os.path.splitext(file.filename)[0]}.pdf')
        convert_image_to_pdf(image_path, pdf_path)

        return redirect(url_for('index'))

def convert_image_to_pdf(image_path, pdf_path):
    # Use a library like pdfkit to convert the image to PDF
    # You need to have wkhtmltopdf installed on your system
    # Install it from: https://wkhtmltopdf.org/downloads.html
    pdfkit.from_file(image_path, pdf_path)

if __name__ == '__main__':
    app.run(debug=True)
