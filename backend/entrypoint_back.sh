#!/bin/bash

mkdir -p /back/log

migrateData=0
#Commande pour générer le modele à partir d'une BDD existante
#  on se position ou il ya manage.py

# python3.7 /back/manage.py inspectdb > back_app/models.py

# python3.7 /back/manage.py migrate


# python3.7 /back/manage.py makemigrations

 python3.10 /back/manage.py migrate --run-syncdb

#if [ "${DJANGO_ENV}" = "local" ]; then
#
#	# Chargement des data initiales
# python3.7 /back/manage.py loaddata initial-data.json
#
#fi

#Commande pour générer le inital data

# python3.7 manage.py dumpdata --format yaml > back_app/fixtures/initial-data.yaml
# python3.7 manage.py dumpdata --format json > back_app/fixtures/initial-data.json
#  a garder en tête que le fait d'ajouter initial-data ne va pas impacter les autres utilisateurs existents deja! seulement si on cange dans les fixtures un utilisateur deja existent, il est change dans l bdd. ça veut dire que djsngo garde aussi une trace des utlisateurs crees par des fixtures
# python3.7 /back/manage.py loaddata initial-data.json

# python3.7 /back/manage.py loaddata initial-data.yaml


python3.10 /back/manage.py runserver 0.0.0.0:${BACK_PORT}


exec "$@"
