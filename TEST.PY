from flask import Flask, render_template, request, jsonify

app = Flask(__name__)  # Corrected app initialization

@app.route('/')
def home():
    return render_template('index.html')  # Ensure index.html exists in the 'templates' folder

@app.route('/generate_resume', methods=['POST'])
def generate_resume():
    data = request.form  # Getting form data

    # Extracting user input
    resume = {
        'full_name': data.get('full_name', ''),
        'phone_number': data.get('phone_number', ''),
        'email': data.get('email', ''),
        'linkedin': data.get('linkedin', ''),
        'website': data.get('website', ''),
        'career_summary': data.get('career_summary', ''),
        'education': {
            'degree': data.get('degree', ''),
            'university': data.get('university', ''),
            'grad_year': data.get('grad_year', ''),
            'coursework': data.get('coursework', ''),
            'gpa': data.get('gpa', '')
        },
        'work_experience': {
            'job_title': data.get('job_title', ''),
            'company': data.get('company', ''),
            'job_duration': data.get('job_duration', ''),
            'responsibilities': data.get('responsibilities', '')
        },
        'skills': {
            'technical_skills': data.get('technical_skills', ''),
            'soft_skills': data.get('soft_skills', '')
        },
        'certifications': data.get('certifications', ''),
        'online_courses': data.get('online_courses', '')
    }

    return jsonify(resume)  # Return JSON response

if __name__ == '__main__':  # Fixed __name__ check
    app.run(debug=True)
