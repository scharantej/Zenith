
# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application
app = Flask(__name__)

# Define the main route
@app.route('/')
def index():
    return render_template('index.html')

# Define the contact route
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # TODO: Send the contact information to a database or email address

    return redirect(url_for('index'))

# Run the application
if __name__ == '__main__':
    app.run(debug=True)
