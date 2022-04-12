# health-application

[![Python Test](https://github.com/dpe22/health-application/actions/workflows/python-test.yml/badge.svg)](https://github.com/dpe22/health-application/actions/workflows/python-test.yml)

## Getting Started
Starting in the root "health-application" folder
> set FLASK_APP=cloudapp
> set FLASK_ENV=development
> flask run
Open a browser and navigate to localhost:5000

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

## DEMO
### Splash page
![image](https://user-images.githubusercontent.com/74585697/160616724-ae141602-1765-4786-aa24-88a505c6c62a.png)

### Register a new user page
![image](https://user-images.githubusercontent.com/74585697/160616998-c19ba3db-d680-4d26-8bc9-ea74d75445b2.png)

### Log in page
![image](https://user-images.githubusercontent.com/74585697/160617334-6cb6dfbf-5939-4579-abb6-c2c08a89e22e.png)

### Logged in as Patient no devices
![image](https://user-images.githubusercontent.com/74585697/160618819-5ebe73ae-7a80-4564-82b9-b37938a23d5c.png)

