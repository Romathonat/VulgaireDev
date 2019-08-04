cd src/static/vulgaireDevEntries/ 
git pull
cd ../../..
docker-compose down
docker-compose build && docker-compose up -d 
