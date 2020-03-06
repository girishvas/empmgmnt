# Employee Management API

This application allows to create department and Employee.
Allow user to perform CRUD operations and filter with department and Salary basis.

### Prerequisites
- GIT
- Python 3.6

### Installation
1. Clone [project](https://github.com/girishvas/empmgmnt.git) repository

`git clone https://github.com/girishvas/empmgmnt.git`

2. Access project directory

`cd empmgmnt`

3. Create a Python Virtualenv and activate it
```
virtualenv env --python python3.6
source .env/bin/activate
```
4. Install project requirements

`pip install -r requirement.txt`

5. Run Database migration

`./manage.py migrate `
6. Create a Superuser to manage the system

`./manage.py createsuperuser`

7. Load Initial data

`./manage.py loaddata initial_load.json `

8. Run the Project

`./manage.py runserver`

9. Get the PostMan link for testing API

`https://www.getpostman.com/collections/57115e50ecf771da1407`

import the collections to the Postman and test the API

10. Swagger documentation also available 

`http://127.0.0.1:8000/`

11. Rest framework url are available here

`http://127.0.0.1:8000/api/emplist/`
