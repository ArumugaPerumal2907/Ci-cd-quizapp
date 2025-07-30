# Mentorbabaa Quiz App

## Overview
The Mentorbabaa Quiz App is a full-stack web application built using Flask, MySQL, and modern web technologies (HTML, CSS, JavaScript). This application allows users to register, log in, take quizzes, and view their results. It also supports uploading quiz questions via Excel files.

## Features
- User registration and authentication
- Dashboard for logged-in users
- Quiz functionality with multiple-choice questions
- Results display after quiz completion
- Admin functionality to upload quiz questions via Excel

## Technologies Used
- **Backend**: Flask, MySQL
- **Frontend**: HTML, CSS, JavaScript
- **Containerization**: Docker
- **CI/CD**: Jenkins, GitHub Actions
- **Deployment**: AWS EC2

## Project Structure
```
apquiz-app
├── apquiz_app
│   ├── __init__.py
│   ├── app.py
│   ├── config.py
│   ├── templates
│   │   ├── index.html
│   │   ├── register.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── upload.html
│   │   ├── quiz.html
│   │   └── results.html
│   └── static
│       ├── css
│       │   └── style.css
│       └── js
│           └── main.js
├── tests
│   └── test_app.py
├── Dockerfile
├── Jenkinsfile
├── requirements.txt
├── .gitignore
├── deploy
│   ├── aws_ec2_deploy.sh
│   └── README.md
├── .github
│   └── workflows
│       └── ci.yml
└── README.md
```

## Setup Instructions
1. **Clone the Repository**
   ```
   git clone <repository-url>
   cd apquiz-app
   ```

2. **Install Dependencies**
   Ensure you have Python and pip installed. Then run:
   ```
   pip install -r requirements.txt
   ```

3. **Configure Database**
   Update the `config.py` file with your MySQL database connection details.

4. **Run the Application**
   To start the Flask application, run:
   ```
   python -m flask run
   ```

5. **Access the Application**
   Open your web browser and navigate to `http://127.0.0.1:5000`.

## CI/CD Pipeline
The project includes a Jenkinsfile for setting up a CI/CD pipeline that automates the build, test, and deployment processes. Ensure Jenkins is configured to monitor the repository for changes.

## Deployment
For deployment, the project includes a script (`aws_ec2_deploy.sh`) that automates the deployment of the Docker container to an AWS EC2 instance.

## Testing
Unit tests are provided in the `tests/test_app.py` file to ensure the application behaves as expected. Run the tests using:
```
pytest tests/
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.