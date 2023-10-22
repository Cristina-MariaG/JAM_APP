# Utiliser une image de base Python
FROM python:3.10

# Définir le répertoire de travail
WORKDIR /back

# Copier le fichier requirements.txt et installer les dépendances
COPY ./requirements.txt /back/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source de l'application
COPY . /back

# Exposer le port sur lequel fonctionne l'application
EXPOSE 8213

# Copy requirements.txt and install dependencies
COPY requirements.txt /tmp/requirements.txt

RUN python3.10 -m pip install --upgrade pip && python3.10 -m pip install -r /tmp/requirements.txt

# Clean up
# RUN rm get-pip.py

# Set the default command to bash
CMD ["bash"]
