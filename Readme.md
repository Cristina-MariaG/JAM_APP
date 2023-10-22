## Getting Started
Clone this repository.
Create a .env file in jam_app and put inside all the content of the jam_app/.env.local file.


### Prerequisites

Requirements for the software and other tools to build, test and push

- [Docker and docker-compose](https://docs.docker.com/get-docker/)


#### Create external networks and volumes

To create the external volumes needed and to create dedicated networks, run the script `setup.sh`.


## Launch the stack

You can then launch the stack simply with `docker-compose up`.

The following urls will be available:

- front : http://localhost:8000/
- back : http://localhost:8213/


## Running the tests in dev mode
Run the tests directly inside the dev containers

Run all the tests  :
- run the container for the back :
 docker exec -it jam-back bash


  python3.7 backend/manage.py test backend/back_app/tests -v 2 
 docker exec -it jam-back bin/bash python3.7 back/back_app/manage.py test back_app/tests -v 2 

-inside the container run :
python3.10 manage.py test back_app/tests -v 2

Run a single test inside a class test
 - python3.10 manage.py test back_app/tests -k <test_name_match_inside_class_test>
 - python3.10 manage.py test back_app/tests -k <test_name_file_without_extension>

 - python3.10 manage.py test back_app/tests -k test_refresh_token (file)
 - python3.10 manage.py test back_app/tests -k test_refresh_token_generate (test name inside test_refresh_token)

 
docker compose exec jam-back python manage.py test