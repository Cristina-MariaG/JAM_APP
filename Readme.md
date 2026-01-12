#JAM Shop
This repository is a starting point for JAM App

Full-Stack Web Application

This project is a complete web application for selling jams, developed as part of the Expert in Computer Science and Information Systems training program at 3W Academy.

The main objective of this project was to transform an existing application into a modern, API-based architecture and to design a dedicated front-end to consume it, with a strong focus on code quality, testing, security, and maintainability.

🔧 Tech Stack

Backend: Django REST Framework (secure REST API)

Frontend: Vue.js 3 + TypeScript

Database: MySQL

Testing: Unit, integration, and end-to-end tests (backend & frontend)

Infrastructure: Docker & Docker Compose

Architecture: Clear separation between Frontend / API / Database

🚀 Key Features

Secure authentication

Advanced faceted search filters

Online payments with Stripe

Versioned and fully tested API

Full application containerization

Detailed technical documentation

This project demonstrates my ability to design, develop, test, and deploy a full-stack web application from start to finish, with an emphasis on clean architecture, code quality, and scalability.

## Getting Started
Clone this repository.

Create a .env file at the root of project and put inside all the content of the .env.local file.

These app needs the keys from an account stripe.

We already have some stripe keys, so to test the application we can use those that are already declared (in .env.local)

### Prerequisites

Requirements for the software :

- [Docker and docker-compose](https://docs.docker.com/get-docker/)


#### Create external networks and volumes

To create the external volumes needed and to create dedicated networks, run the script `setup.sh`.


## Launch the stack

You can then launch the stack simply with `docker-compose up`.

The following urls will be available:

- front : http://localhost:8000/
- back : http://localhost:8213/


To connect as admin :
email : admin@admin.com
password :adminlovejam

## Running the tests in dev mode
Run the tests directly inside the dev containers

Frontend :
- run in front/ folder (cd front):
docker exec jam-front npm run test 

- npm run test        (to run all the tests)
- npm run watch        (to run all the tests but keep alive to track changes)
- npm run coverage     (for coverage report)
- npm run test:unit fileName -- --watch       (to run a single test)


Backend :

Run all the tests  :
- run the container for the back :
 docker exec -it jam-back bash


-inside the container run :
python3.10 manage.py test back_app/tests -v 2

Run a single test inside a class test
 - python3.10 manage.py test back_app/tests -k <test_name_match_inside_class_test>
 - python3.10 manage.py test back_app/tests -k <test_name_file_without_extension>

 - python3.10 manage.py test back_app/tests -k test_refresh_token (file)
 - python3.10 manage.py test back_app/tests -k test_refresh_token_generate (test name inside test_refresh_token)

 or run tests with one line with :
 docker exec jam-back  python3.10 manage.py test back_app/tests -v 2



