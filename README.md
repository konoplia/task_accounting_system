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

