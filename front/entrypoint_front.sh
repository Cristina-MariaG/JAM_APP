#!/bin/bash
cd /front

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
  
  fi

exec "$@"