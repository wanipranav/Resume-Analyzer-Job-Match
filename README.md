🧠 AI-Powered Resume Analyzer & Job Match Platform

A full-stack web application that analyzes resumes and matches them against job descriptions using ATS-style keyword analysis. The platform provides match scores, missing skills, keyword gaps, and actionable improvement suggestions to help candidates optimize their resumes for specific roles.


🚀 Features

📄 Upload resumes in PDF, DOCX, or TXT format

📝 Paste or upload job descriptions

📊 Match score (0–100) based on keyword overlap

🧩 Missing skills & keywords identification

💡 Resume improvement feedback & suggestions

🔐 Secure file handling with size and type validation

🧱 Modular backend architecture (easy to extend with AI/ML)



🏗️ System Architecture
Frontend

HTML, CSS, JavaScript

Simple and intuitive UI for resume upload and analysis

Results displayed with clear sections (score, gaps, feedback)

Backend

Python + Flask

Handles file uploads, text extraction, and analysis logic

Clean separation of concerns using utility modules

Core Modules

text_extract.py

Extracts text from PDF, DOCX, and TXT files

scoring.py

Performs ATS-style keyword matching

Extracts skills, computes overlap, and generates feedback



🗂️ Project Structure
Resume-Analyzer-Job-Match/
│
├── app.py                  # Flask application entry point
├── requirements.txt        # Python dependencies
├── nixpacks.toml           # Production start command (deployment-ready)
│
├── templates/
│   ├── index.html          # Upload & input page
│   └── results.html        # Analysis results page
│
├── static/
│   ├── style.css           # Styling
│   └── app.js              # Frontend logic
│
├── utils/
│   ├── text_extract.py     # Resume/JD text extraction
│   └── scoring.py          # Keyword matching & scoring logic
│
└── uploads/                # Temporary file storage (ignored in Git)



⚙️ How the Matching Works (MVP Logic)

Resume and Job Description text is normalized

Stopwords are removed

Keywords are extracted based on frequency

Resume keywords are compared with JD keywords

A match score is calculated

Missing keywords and skills are identified

Feedback and suggestions are generated

This design is deployment-ready and can be upgraded to semantic AI matching using embeddings.



▶️ How to Run Locally
1️⃣ Clone the repository
git clone https://github.com/wanipranav/Resume-Analyzer-Job-Match.git
cd Resume-Analyzer-Job-Match

2️⃣ Create and activate virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Run the application
python app.py

5️⃣ Open in browser
http://127.0.0.1:5000



🧪 Sample Use Case

Upload your resume (PDF/DOCX)

Paste a job description

Instantly get:

Match score

Missing skills

Keyword gaps

Resume improvement tips



🔒 Security & Constraints

Max file size: 5 MB

Allowed formats only: PDF, DOCX, TXT

Temporary uploads (not committed to Git)

Local-only execution (safe for testing and demos)

🛠️ Future Enhancements

Semantic AI matching using embeddings (BERT / OpenAI)

Resume vs multiple job ranking

PDF report export

User authentication & history

Cloud deployment (Render / Railway)



📌 Why This Project Matters

This project demonstrates:

Full-stack development skills

Backend API design with Flask

File handling & data processing

Practical ATS resume optimization logic

Clean, extensible system architecture