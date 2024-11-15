import os
from flask import Flask, render_template, request

app = Flask(__name__)

UPLOAD_FOLDER = os.path.join(os.path.dirname(__file__), 'tmp')
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        file = request.files.get("file")
        if file and file.filename:
            file_path = os.path.join(UPLOAD_FOLDER, file.filename)
            try:
                file.save(file_path)
                return f"File {file.filename} uploaded successfully and saved to {file_path}."
            except Exception as e:
                return f"An error occurred: {str(e)}"
        else:
            return "No file uploaded."
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
