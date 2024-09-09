from flask import Flask, request, redirect, render_template
import os

app = Flask(__name__)

# Path to the notes file
NOTES_FILE = 'notes.txt'

# Ensure the notes file exists
if not os.path.exists(NOTES_FILE):
    open(NOTES_FILE, 'w').close()

# Route for the home page
@app.route('/')
def index():
    with open(NOTES_FILE, 'r') as file:
        notes = file.readlines()
    return render_template('index.html', notes=notes)

# Route for submitting a note
@app.route('/submit', methods=['POST'])
def submit():
    note = request.form['note']
    with open(NOTES_FILE, 'a') as file:
        file.write(note + '\n')
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
