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
    User will be able to register and login. <br />
Year-service: <br />
    User can add year. <br />
exam-type-service: <br />
    User can add exam type,subject and keyword. <br />
question-service: <br />
    User can add question. <br />
category-service: <br />
    Question will be categorized based on subject and keyword. <br />

**Monolithic Architecture:** <br />
    
**Installation:** <br />
Python-https://www.python.org/downloads/ <br />
Flask- pip install Flask <br />
PyJWT-pip install PyJWT <br />
Werkzeug-pip install Werkzeug <br />
Flask-SQLAlchemy-pip install Flask-SQLAlchemy <br />
git bash insatllation-https://git-scm.com/downloads  <br />
Docker desktop-https://docs.docker.com/get-started/get-docker/ <br />
   &nbsp; Make sure WSL and virtualisation is enabled for docker. <br />
   &nbsp; Steps to enable WSL: <br />
   &nbsp; Steps to enable virtualisation: <br />
SQLlite-https://www.sqlite.org/download.html![image](https://github.com/user-attachments/assets/f8a08b50-ed99-4558-abc5-cd3c09cbeeeb) <br />

**Project execution steps: <br />**

**Project execution using docker:**  <br />
Created docker file for each application service.  <br />
Created docker-compose.yml file to execute all services in containers  <br />
Run below command in git bash  <br />


