#!/bin/bash
cd /front

#A executer en cas d'erreur au lancement
#npm install -g n
#n latest
#npm install -g npm
#hash -d npm
#npm i 

if [ "${VUE_APP_ENV}" != "local" ]; then

  echo "Environnement : Production"
  npm install
  npm run build
  service apache2 restart
  tail -f /dev/null
else
  echo "Environnement : Local"
  npm install
  npm run dev 
  tail -f /dev/null
  # --add-host jam-moteur:51.15.222.143
  # CMD ["nodemon", "--exec", "npm", "run", "docker-start"]
fi

exec "$@"
