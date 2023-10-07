FROM ubuntu:18.04

# PYTHON 3
RUN apt-get update -y
RUN apt-get upgrade -y
RUN apt-get install build-essential -y
RUN apt install -y python3.7
RUN apt-get update -y
RUN apt-get install -y libpython3.7-dev python-numpy

# FOR MYSQL
RUN apt-get update -y && apt-get upgrade -y
RUN apt-get install -y default-libmysqlclient-dev build-essential
RUN apt-get install -y libssl-dev
RUN apt-get install -y wget

# PIP
RUN apt-get install -y python3-pip
RUN python3.7 -m pip install --upgrade pip

# LIBRARIES
RUN pip3 install django==3.2.9
RUN pip3 install djangorestframework==3.12.4
RUN pip3 install django-filter==21.1
RUN pip3 install python-arango==7.2.0
RUN pip3 install pandas==1.3.5
RUN pip3 install mysqlclient==2.0.3
RUN pip3 install mysql-connector-python==8.0.33
RUN pip3 install pyyaml==6.0
RUN pip3 install django-cors-headers==3.10.0
RUN pip3 install rest_framework_simplejwt==0.0.2


