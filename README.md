# StudentPulse — Student Performance Analyzer

A beginner-friendly Python Flask website. Students enter their own details, subject marks, attendance, assignment completion and daily study hours. The app calculates an average, assigns a simple grade band, highlights strongest/weakest subjects and gives practical study suggestions.

## Requirements
- Python 3.9 or newer
- Internet connection for the first install (Flask). Google Fonts are optional; the page has fallback fonts.

## Run on Windows
1. Extract the ZIP folder.
2. Open the extracted `student_performance_analyzer` folder in VS Code.
3. Open Terminal in that folder.
4. Run:
   ```bash
   py -m pip install -r requirements.txt
   py app.py
   ```
5. Open the local address printed in the terminal (usually http://127.0.0.1:5000).

You can also double-click `run.bat` if Python is installed and the `py` command works.

## How to use
- Enter name and roll number.
- Enter at least one subject and marks out of 100. Use **Add another subject** for more subjects.
- Enter attendance %, assignment completion %, and average daily study hours.
- Click **Analyze my performance**.
- Use **Print / Save report** to print or save the result as PDF from your browser.

## Project structure
- `app.py` — Flask routes, validation, calculations and suggestions
- `templates/index.html` — website form and results page
- `static/style.css` — responsive styling
- `requirements.txt` — Python dependency
- `run.bat` — Windows startup helper

## Notes
This is an educational self-assessment tool. Its grade bands and suggestions are illustrative, not an official college grading policy. The app does not store student data in a database; the entered values are processed for the current result only.
