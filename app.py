from flask import Flask, request, redirect, render_template
from markupsafe import Markup
import os
from datetime import datetime

app = Flask(__name__)

NOTES_FILE = "data/notes.txt"

@app.route('/')
def index():
    with open(NOTES_FILE, 'r') as file:
        notes = file.readlines()
    return render_template('index.html', notes=notes)

# Route for submitting a note
@app.route('/submit', methods=['POST'])
@app.route('/submit', methods=['POST'])
def submit():
    current_datetime = datetime.now()
    formatted_datetime = f"<i>{current_datetime.strftime('%Y-%m-%d %H:%M:%S')}</i>"
    note = request.form['note'].strip().replace("\n", " ").replace("\r", " ")
    note = f"<b>{note}</b>"
    sign = request.form['sign'].strip()
    if not sign:
        signature = "<i>Anonymous</i>"
    else:
        signature = f"<i>{sign}</i>"
    with open(NOTES_FILE, 'a') as file:
        file.write(note + " - " + signature + ", " + formatted_datetime + '\n')
    return redirect('/')


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/links')
def links():
    return render_template('links.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
