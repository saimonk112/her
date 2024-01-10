# app.py

from flask import Flask, render_template, make_response
import pdfkit

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, Flask World!'

@app.route('/generate_pdf')
def generate_pdf():
    pdfkit.from_url('https://www.google.com', 'output.pdf')  # Replace with your actual Heroku URL
    response = make_response(open('output.pdf', 'rb').read())
    response.headers['Content-Type'] = 'application/pdf'
    response.headers['Content-Disposition'] = 'inline; filename=output.pdf'
    return response

if __name__ == '__main__':
    app.run(debug=True)

