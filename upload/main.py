from flask import Flask , render_template, request, send_from_directory, redirect, url_for
from werkzeug.utils import secure_filename
from werkzeug.exceptions import RequestEntityTooLarge
import os

app = Flask(__name__)
app.config["UPLOADS_DIR"] = "uploads/"
app.config["MAX_CONTENT_LENGTH"] = 16 *1024 *1024
app.config["ALLOWED_EXTENSIONS"] = [".jpg", ".jpeg", ".png", ".gif"]

@app.route("/")
def index():
    images = []
    files = os.listdir(app.config["UPLOADS_DIR"])
    for file in files:
        extension =os.path.splitext(file)[1].lower()
        if extension in app.config["ALLOWED_EXTENSIONS"]:
            images.append(file)
    return render_template("index.html", images=images)

@app.route("/upload", methods=["POST"])
def upload():
    if request.method == "POST":
        try:
            file = request.files["file"]
            extension = os.path.splitext(file.filename)[1].lower()
            if file:
                if extension in app.config["ALLOWED_EXTENSIONS"]:

                    file.save(os.path.join(app.config["UPLOADS_DIR"], secure_filename(file.filename)))
                    return redirect(url_for("index"))
                else:
                    return f"<h3>{file.filename} is not an image. Only images cann be uploaded</h3"
            else:
                return "<h3>A file  to be uploaded is required</h3>"
        except RequestEntityTooLarge:
            return f"<h3> {file.filename} is larger than the expected size of uploads</h3>"


@app.route("/view_image/<filename>", methods=["GET"])
def view_image(filename):
    return send_from_directory(app.config["UPLOADS_DIR"], filename)


if __name__  == "__main__":
    app.run(debug=True)