## Flask Application Design for File Selector and Google Cloud Storage Upload

## HTML Files
- **index.html**:
   - Contains a file selector input element for choosing a file to upload.
   - Has a submit button to trigger the upload process.

## Routes
- **GET /**:
   - Renders the `index.html` file.

- **POST /upload**:
   - Handles the file upload process:
     - Retrieves the uploaded file from the request.
     - Generates a unique file name and path for the uploaded file in the Google Cloud Storage bucket.
     - Uploads the file to the specified bucket using the Google Cloud client library.
     - Redirects to a success page or displays an error message if the upload fails.