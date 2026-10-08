from flask import Flask, render_template

app = Flask(__name__)

# Mock database of placement drives
placement_drives = [
    {
        "company": "TechCorp Solutions",
        "role": "Software Engineer Intern",
        "eligibility": "B.Tech (CSE/IT) with CGPA > 8.0, No active backlogs",
        "package": "12 LPA",
        "deadline": "October 25, 2026",
        "contact": "placement.cse@college.edu"
    },
    {
        "company": "Innovate Analytics",
        "role": "Data Analyst",
        "eligibility": "B.Tech (All Branches), MCA with basic SQL knowledge",
        "package": "8 LPA",
        "deadline": "November 02, 2026",
        "contact": "placement.cell@college.edu"
    }
]

@app.route('/')
def home():
    portal_info = {
        "college_name": "Apex Institute of Technology",
        "department": "Department of Computer Science & Engineering"
    }
    return render_template('index.html', portal=portal_info, drives=placement_drives)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
