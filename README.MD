     Student Attendance Tracker — Cloud‑Native Application

A cloud‑native Student Attendance Tracking system built using Flask, MySQL, HTML/CSS/JS, and deployed on an AWS EC2 Ubuntu instance.  

This project demonstrates backend API development, frontend UI design, database integration, and cloud deployment.


     Project Structure


attendance-system/
│
├── backend/
│   ├── app.py
│   ├── auth.py
│   ├── controllers/
│   ├── routes/
│   ├── db/
│   ├── test_db.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── login.html
│   ├── dashboard.html
│   ├── admin_*.html
│   ├── student_*.html
│   ├── teacher_*.html
│   ├── styles.css
│   └── main.js
│
└── README.md



 Purpose of the Project

The goal of this project is to design and deploy a Cloud‑native Attendance Tracking System that allows:

- Students to mark attendance  
- Teachers to manage classes  
- Admins to manage students, teachers, and courses  
- Real‑time communication between frontend and backend  
- Secure authentication  
- Persistent storage using MySQL  

The system is deployed on `AWS EC2`, demonstrating cloud hosting, Linux server management, and production‑ready configuration.



   Technologies Used

   Backend
- Python 3  
- Flask  
- MySQL Connector  
- JWT Authentication  
- REST API Architecture  

  Frontend
- HTML  
- CSS  
- JavaScript  
- Fetch API  

   Database
- MySQL 8.0  
- Hosted on AWS EC2  

     Cloud
- AWS EC2 (Ubuntu 24.04)  
- Security Groups  
- Linux environment  
- Git + GitHub version control  



     Backend Setup (EC2)

1. Clone the repository

git clone https://github.com/sorina-antonia/attendance-system.git
cd attendance-system/backend


2. Create virtual environment

python3 -m venv venv
source venv/bin/activate


3. Install dependencies

pip install -r requirements.txt


4. Configure environment variables
Create a `.env` file:

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=attendance
SECRET_KEY=yourjwtsecret


5. Run backend

python app.py


Backend runs on:

http://<EC2-Public-IP>:5000



   Frontend Setup

Upload the `frontend/` folder to the EC2 instance or host locally.

To run locally:

open index.html


To run on EC2 using Python:

python3 -m http.server 8080


Frontend runs on:

http://<EC2-Public-IP>:8080



API Endpoints (Examples)

   Authentication
- POST /login
- POST /register

    Students
- GET /students
- POST /students
- PUT /students/<id>
- DELETE /students/<id>

    Attendance
- `POST /attendance/mark`
- `GET /attendance/student/<id>`



Screenshots


AWS Deployment Summary

This project was deployed on an **AWS EC2 Ubuntu instance:

- EC2 instance created using AWS Academy  
- Security groups configured for ports 22, 5000, 8080  
- MySQL installed and configured  
- Backend and frontend uploaded  
- Git installed and connected to GitHub  
- Code pushed from EC2 → GitHub using a Personal Access Token  


Version Control (GitHub)

This repository contains:

- Full backend source code  
- Full frontend UI  
- Project documentation  
- Version history  

GitHub was used for:

- Tracking changes  
- Backing up the project  
- Submitting the final assignment  
- Maintaining clean project structure  


Author:
 Student ID: HE26720