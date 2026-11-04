from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)

def grade_for(avg):
    if avg >= 90: return "A+", "Excellent"
    if avg >= 80: return "A", "Very Good"
    if avg >= 70: return "B", "Good"
    if avg >= 60: return "C", "Average"
    if avg >= 40: return "D", "Needs Improvement"
    return "F", "At Risk"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None
    if request.method == "POST":
        try:
            name = request.form.get("name", "").strip()
            roll = request.form.get("roll", "").strip()
            subjects = request.form.getlist("subject[]")
            marks_raw = request.form.getlist("marks[]")
            attendance = float(request.form.get("attendance", "0"))
            assignment = float(request.form.get("assignment", "0"))
            study_hours = float(request.form.get("study_hours", "0"))

            if not name or not roll:
                raise ValueError("Please enter the student's name and roll number.")
            if not subjects or len(subjects) != len(marks_raw):
                raise ValueError("Please add at least one subject with marks.")
            marks = []
            for subject, raw in zip(subjects, marks_raw):
                value = float(raw)
                if not subject.strip():
                    raise ValueError("Subject names cannot be empty.")
                if not 0 <= value <= 100:
                    raise ValueError("Marks must be between 0 and 100.")
                marks.append({"subject": subject.strip(), "marks": value})
            if not 0 <= attendance <= 100 or not 0 <= assignment <= 100:
                raise ValueError("Attendance and assignment completion must be between 0 and 100.")
            if not 0 <= study_hours <= 24:
                raise ValueError("Daily study hours must be between 0 and 24.")

            average = sum(x["marks"] for x in marks) / len(marks)
            grade, performance = grade_for(average)
            strongest = max(marks, key=lambda x: x["marks"])
            weakest = min(marks, key=lambda x: x["marks"])
            tips = []
            if attendance < 75:
                tips.append("Attendance is below 75%. Try to attend classes regularly and check your college's attendance policy.")
            if assignment < 70:
                tips.append("Complete pending assignments and submit them before the deadline.")
            if weakest["marks"] < 60:
                tips.append(f"Give extra revision time to {weakest['subject']} and practise a few questions every day.")
            if study_hours < 1:
                tips.append("Build a consistent study routine. Start with a focused 30–45 minute session.")
            elif study_hours < 2:
                tips.append("If your schedule allows, gradually add another focused study session.")
            if not tips:
                tips.append("Keep up the consistent work. Revise weekly and solve practice questions to maintain your progress.")
            result = {
                "name": name, "roll": roll, "average": round(average, 1),
                "grade": grade, "performance": performance, "attendance": round(attendance, 1),
                "assignment": round(assignment, 1), "study_hours": round(study_hours, 1),
                "subjects": marks, "strongest": strongest, "weakest": weakest, "tips": tips
            }
        except ValueError as exc:
            error = str(exc)
        except Exception:
            error = "Please check all the values and try again."
    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)
