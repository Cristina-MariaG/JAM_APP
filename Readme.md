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

- front : http://localhost:8080/
- back :http://localhost:8213/
