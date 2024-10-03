# Question-categorization-System 
Below code repository contains all the supporting project files necessary to implement question categorization system using microservice and monolithic architecture.   <br />

https://github.com/Bhuvaneswari-J/question-categorization-service   <br />
https://github.com/Bhuvaneswari-J/Monolithic-Question-Categorizaton-system    <br />

**Project Group (65): <br />**
Aparna Pundir(M23AID006) <br />
Bhuvaneswari J(M23AID053) <br />

**Project Demo link:** <br />

https://drive.google.com/file/d/1X6jasvn2hFvVeoLRYhJpr9caW8F9yTUG/view?usp=sharing   <br />

**About Project:** <br />
This project focuses on categorising questions based on the subject and keywords added for a exam type. <br />
Steps: <br />
      &nbsp; User can register and login <br />
      &nbsp; User can year,exam type,subject,keyword and question. <br />
      &nbsp; Questions will be categorised based on subject and keyword and shared as result. <br />
      
**Microservice Architecture:** <br />
Question categorization microservice architecture consist of below microservices: <br />
User-service: <br />
   &nbsp;&nbsp; User will be able to register and login. <br />
Year-service: <br />
   &nbsp;&nbsp; User can add year. <br />
exam-type-service: <br />
   &nbsp;&nbsp; User can add exam type,subject and keyword. <br />
question-service: <br />
   &nbsp;&nbsp; User can add question. <br />
category-service: <br />
   &nbsp;&nbsp; Question will be categorized based on subject and keyword. <br />

**Monolithic Architecture:** <br />
    All services will be combined in one single application.
    
**Installation:** <br />
Python-https://www.python.org/downloads/ <br />
Flask- pip install Flask <br />
PyJWT-pip install PyJWT <br />
Werkzeug-pip install Werkzeug <br />
Flask-SQLAlchemy-pip install Flask-SQLAlchemy <br />
git bash insatllation-https://git-scm.com/downloads  <br />
Docker desktop-https://docs.docker.com/get-started/get-docker/ <br />
   &nbsp; Make sure WSL and virtualisation is enabled for docker. <br />
SQLlite-https://www.sqlite.org/download.html![image](https://github.com/user-attachments/assets/f8a08b50-ed99-4558-abc5-cd3c09cbeeeb) <br />

**Project execution steps: <br />**

**Project execution using docker:**  <br />
Created docker file for each application service.  <br />
Created docker-compose.yml file to execute all services in containers  <br />
Run below command in git bash  <br />
  &nbsp;  &nbsp; docker-compose up --build   <br />
Use docker ps command to view container port details.   <br />
Use below curl command to add and verify value.  <br />

curl -X POST http://localhost:5001/register -H "Content-Type: application/json" -d '{"username": "newuser11", "password": "password123"}'   <br />

curl -X POST http://localhost:5001/login -H "Content-Type: application/json" -d '{"username": "newuser11", "password": "password123"}'   <br />

curl -X POST http://localhost:5002/year -H "Content-Type: application/json" -d '{"year_value": "2024"}'   <br />

curl -X POST http://localhost:5003/exam-type -H "Content-Type: application/json" -d '{"name": "UPSC"}'   <br />

curl -X POST http://localhost:5003/subject -H "Content-Type: application/json" -d '{"name": "Geography", "exam_type_id": 1}'   <br />

curl -X POST http://localhost:5003/keyword -H "Content-Type: application/json" -d '{"value": "River", "subject_id": 1}'   <br />

curl -X POST http://localhost:5004/question -H "Content-Type: application/json" -d '{"text": "Explain Himalayan river system.", "exam_year_id": 1, "exam_type_id": 1}'   <br />

curl http://localhost:5000/categorize/1   <br />

