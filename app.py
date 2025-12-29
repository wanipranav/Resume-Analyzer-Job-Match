import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from dotenv import load_dotenv

from utils.text_extract import extract_text_from_file
from utils.scoring import analyze_match

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")

ALLOWED_EXTENSIONS = {"pdf", "docx", "txt"}

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = 5 * 1024 * 1024  # 5 MB limit


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    # Resume file
    resume_file = request.files.get("resume")
    if not resume_file or resume_file.filename.strip() == "":
        return "Resume file missing", 400
    if not allowed_file(resume_file.filename):
        return "Unsupported resume file type. Use PDF/DOCX/TXT.", 400

    os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
    resume_filename = secure_filename(resume_file.filename)
    resume_path = os.path.join(app.config["UPLOAD_FOLDER"], resume_filename)
    resume_file.save(resume_path)

    # Job description (textarea OR file)
    jd_text = (request.form.get("job_description") or "").strip()

    jd_file = request.files.get("job_file")
    if jd_file and jd_file.filename.strip():
        if not allowed_file(jd_file.filename):
            return "Unsupported JD file type. Use PDF/DOCX/TXT.", 400
        jd_filename = secure_filename(jd_file.filename)
        jd_path = os.path.join(app.config["UPLOAD_FOLDER"], jd_filename)
        jd_file.save(jd_path)
        jd_text = extract_text_from_file(jd_path)

    if not jd_text:
        return "Job description missing (paste text or upload file).", 400

    resume_text = extract_text_from_file(resume_path)

    results = analyze_match(resume_text, jd_text)

    return render_template("results.html", results=results, resume_name=resume_filename)


if __name__ == "__main__":
    app.run(debug=True)
