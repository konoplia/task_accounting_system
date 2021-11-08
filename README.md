# Task accounting system

# Description
Task accounting system
it is a system that allows users to create, view, edit, and delete tasks. 
Users register in the service, then the administrator adds users to the appropriate groups (Managers or Developers)
Managers can create tasks, edit and delete. Can assign created tasks to developers.
Developers in tasks assigned to them can edit only the task completion status.

# Installation

```bash
https://github.com/konoplia/task_accounting_system.git
```
Docker must be installed on your computer to run the application.\
How to install docker see here:
https://docs.docker.com/\
When docker is installed and the application is downloaded, go to the root directory of the project
```bash
.
├── Dockerfile
├── authentication
├── celerybeat-schedule
├── docker-compose.yml
├── logs
├── main_app
├── manage.py
├── my_project_visualized.dot
├── requirements.txt
└── task_accounting_sys
```
and run
```bash
docker-compose up
```
Now that the docker containers are running, we can use the application through the API interface.

# Usage
### Register
The first thing a user needs to do is register:
```bash
 curl --header "Content-Type: application/json" --request POST --data '{"username":"test_manager","password":"test_manager"}' http://localhost:8000/api/register/
```
Server response is:
```bash
{"success":"User 'test_manager' created successfully"}
```
### Get token
Then the registered user needs to get an access token, at the address http://127.0.0.1:8000/api/token/  using the post method send credentials:
```bash
 curl --header "Content-Type: application/json" --request POST --data '{"username":"test_manager","password":"test_manager"}' http://localhost:8000/api/token/

```
Server response:
```bash
{"refresh":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYzNjU0OTY2MCwianRpIjoiYTliZTc3YmMyOGIyNGJmZGFiMzYxMWJhOTY5OTM5Y2IiLCJ1c2VyX2lkIjo3fQ.ywB739ORfFKs4aYu
FSg1VfahyNwTDGJoKnSccv29z7g","access":"eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NDYzMjYwLCJqdGkiOiJkMGE1NzBjNWM1YzE0M2Y0ODMzZjZjNDBlODQxZDJjNyIsInVzZXJf
aWQiOjd9.3qFCws3RdNybpxWR94yG4wgMhzmn41rY6qA9qlexN5k"}
```
### Create task
Only after the administrator adds the user to the Managers group, the user can create tasks. Required fields for the task are "name" and "description"
```bash
curl --header 'Content-Type: application/json' --header 'Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjM2NDcyNDMzLCJqdGkiOiJmYTNhMTE5MTQ3YjA0M2JiODFjODgyZTA2NTllZmE1OSIsInVzZXJfaWQiOjd9.6EY5F2cdH2vzmAa7RG4xhHrhzGbnSCSM2b8AH2uURvg' --request POST --data '{"name":"test task","description":"test description"}'  http://localhost:8000/api/tasks/create/
```

Server response:
```bash
{"success":"Task 'test task' created successfully"}
```
### Tasks list
```bash
curl http://localhost:8000/api/tasks/
```
Server response:
```bash
{
"id":1,
"name":"test task",
"description":"test description",
"create_date":"2021-11-08T18:07:43.444091+02:00",
"status":1,
"priority":1,
"life_time":1,
"created_by":7,
"executor":null
}
```
Fields: "id", "created_at", "created_by" are auto fields.\
Fields "status","priority", "life_time" have default values, but can be changed by manager.\
Field "executor" can be "null"


# UML diagrams
#### Entities relations diagram
![entities_relations_diagram](images/uml_diagrams/entities_relations_diagram.jpg)
#### Internal-services rejections diagram
![internal-services rejections_diagram](images/uml_diagrams/internal-services%20rejections_diagram.jpg)
