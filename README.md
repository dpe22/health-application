# health-application

[![Python Test](https://github.com/dpe22/health-application/actions/workflows/python-test.yml/badge.svg)](https://github.com/dpe22/health-application/actions/workflows/python-test.yml)

## Getting Started (Local Shell Version #1)
Make sure you have windows-curses module installed if on Windows

Launch interface.py from the local shell folder

credentials.txt stores usernames and hashed passwords

devices.db stores device information

users.db stores user information


### Demo Local V1
###### Splash Terminal
![image](https://user-images.githubusercontent.com/74585697/165771008-40309cf6-e9b7-4255-a34f-578a97f482b1.png)

###### Register a new user
![image](https://user-images.githubusercontent.com/74585697/165771557-f2ca4b1a-bef4-4869-b269-1f3682f39f77.png)

###### Logged in
![image](https://user-images.githubusercontent.com/74585697/165771975-071fed95-ce02-4b1c-81bb-1530fe311817.png)

###### Add a device
![image](https://user-images.githubusercontent.com/74585697/165773752-a920580c-e4f4-4ca4-a259-118ba479b41e.png)


## Getting Started (Web App Version #2)
Starting in the root "health-application" folder

> set FLASK_APP=cloudapp

> set FLASK_ENV=development

> flask init-db

> flask run

Open a browser and navigate to localhost:5000

## Architecture 

### DB Schema Planned
![HealthApp](https://user-images.githubusercontent.com/74585697/155168764-15864e0d-f2d6-426c-9106-7aa4f0234526.png)

### DB Schema Actual
![image](https://user-images.githubusercontent.com/74585697/162868839-248733f5-2924-4e9e-aff8-fb243db1b2a4.png)

### User Stories

#### Admin
- add users
- assign and change user roles
- connect third party devices to monitor patients with devices (thermometer, pulse blood pressure, glucometer, etc)
- enable or disable any third party (developer, device-owner)

#### Practitioner
- browse patients
- assign medical devices to patients
- schedule device measurements and alerts

####
use AWS virtual machine EC2

## SQLite3 Database

![image](https://user-images.githubusercontent.com/74585697/162985742-79879422-3463-4847-8483-af2009b78f65.png)

## DEMO
### Splash page
![image](https://user-images.githubusercontent.com/74585697/160616724-ae141602-1765-4786-aa24-88a505c6c62a.png)

### Register a new user page
![image](https://user-images.githubusercontent.com/74585697/160616998-c19ba3db-d680-4d26-8bc9-ea74d75445b2.png)

### Log in page
![image](https://user-images.githubusercontent.com/74585697/160617334-6cb6dfbf-5939-4579-abb6-c2c08a89e22e.png)

### Logged in as Patient no devices
![image](https://user-images.githubusercontent.com/74585697/160618819-5ebe73ae-7a80-4564-82b9-b37938a23d5c.png)

### Logged in as Patient w/devices
Still working on making sure that device table is not subject to vulnerabilities below. While testing I accidentally deleted the table, easy to fix. I am also working on making sure that the user experience is different for admin, patient, practitioner and engineer roles: specifically that each role sees only devices assigned to that role. 

## Vulnerabilities
### SQL Injection
Although the login interaction is safe, once logged in the database tables are vulnerable to SQL injection. Note here the database locking after tring to add a device with DROP TABLE in the name field.

![image](https://user-images.githubusercontent.com/74585697/162985231-449e88d3-f959-45ba-8a0e-14973026f2fe.png)

## Deployment
Attempted to containerize the application using Docker and deploy to AWS Lightsail. Went down a rabbit hole with trying to change my weebly domain monkeyselfies.com to run the containerized application by modifying the DNS record to point back to AWS. Very messy. Probably much easier to deploy using AWS EC2. Work in progress. 
