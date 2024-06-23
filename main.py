
# main.py

from flask import Flask, request, redirect, url_for
from google.cloud import storage

# Initialize Flask app
app = Flask(__name__)

# Google Cloud Storage settings
CLOUD_STORAGE_BUCKET = 'YOUR_BUCKET_NAME'  # Set your bucket name

# Define routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Handle file upload
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            # Generate unique file name and path
            unique_file_name = uploaded_file.filename
            cloud_storage_file_path = f'uploads/{unique_file_name}'

            # Upload file to Google Cloud Storage
            try:
                storage_client = storage.Client()
                bucket = storage_client.get_bucket(CLOUD_STORAGE_BUCKET)
                blob = bucket.blob(cloud_storage_file_path)
                blob.upload_from_string(
                    uploaded_file.read(),
                    content_type=uploaded_file.content_type
                )
                return redirect(url_for('success'))
            except Exception as e:
                return redirect(url_for('error'))
    return render_template('index.html')

@app.route('/success')
def success():
    return 'File uploaded successfully!'

@app.route('/error')
def error():
    return 'Error uploading file!'

if __name__ == '__main__':
    app.run(debug=True)
