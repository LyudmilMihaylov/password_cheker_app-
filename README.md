# 🔐 Password Strength Checker – DevOps Project

## 📌 Project Overview

This project demonstrates a **DevOps workflow** by developing a simple **Password Strength Checker** CLI application using **Python**, integrating it with a **SQLite database**, and deploying it via a **CI/CD pipeline** using **GitHub**, **Docker**, **Jenkins**, **Terraform**, and **AWS EC2**.

The solution covers:

- ✅ Test-Driven Development (TDD)
- ✅ Source Code Management (SCM) with Git and GitHub
- ✅ CI/CD automation with Jenkins
- ✅ Containerization with Docker
- ✅ Infrastructure-as-Code with Terraform
- ✅ Integration with a database (SQLite)
- ✅ DevOps principles such as branching, abstraction, and refactoring

---

## 🧠 Features

- Checks password strength based on length, numbers, symbols, and upper/lowercase letters
- Saves evaluation history into an SQLite database
- Supports automated unit testing with Python's `unittest`
- Dockerized for portability and repeatability
- Jenkins pipeline automates test, build, push, and deployment
- Terraform provisions infrastructure on AWS

---

## 📂 Project Structure
password-checker/
├── app.py # Main application logic
├── db.py # SQLite database functions
├── test_app.py # Unit tests (TDD)
├── requirements.txt # Python dependencies
├── Dockerfile # Docker config
├── Jenkinsfile # Jenkins pipeline
├── infra/ # Terraform scripts
│ ├── main.tf
│ ├── variables.tf
│ └── outputs.tf
└── README.md


---

## 🧪 Technologies Used

| Tool        | Purpose                                 |
|-------------|------------------------------------------|
| Python      | Core programming language                |
| SQLite      | Lightweight relational database          |
| Docker      | Containerization                         |
| GitHub      | Source code hosting                      |
| Jenkins     | CI/CD automation                         |
| Terraform   | Infrastructure as Code                   |
| AWS EC2     | Cloud infrastructure                     |

---

## ⚙️ Installation and Usage

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/password-checker.git
cd password-checker
2. Run tests (TDD)
bash
Copy
Edit
python3 -m unittest test_app.py
3. Build and run Docker image
bash
Copy
Edit
docker build -t password-checker .
docker run -it password-checker
4. Use the CLI
You'll be prompted to enter a password. The result is saved in the passwords.db SQLite database.



