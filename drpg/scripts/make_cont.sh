#!/bin/bash
# first run docker create
docker container stop $1
docker rm $1
#docker create --name $1 -w /app ubuntu python3 replacer.py
#docker create -it --name $1 -w /app ubuntu /bin/bash /app/user_entrypoint.sh
#docker create -it --name $1 -e "VIRTUAL_HOST=$1" -w /app --expose 80 --network=drpg_app drpg_drpg /bin/bash
docker create -it --name $1 -w /app --expose 80 --network="drpg_app" drpg_drpg /bin/bash /app/user_entrypoint.sh
# then run docker cp
docker cp /app/default/user_entrypoint.sh $1:/app
docker cp /app/make_dj/drpg_template/user_project/. $1:/app
docker cp /app/configs/$1.json $1:/app/replace.json
docker cp /app/default/replacer.py $1:/app/replacer.py
# then run docker exec
docker container start $1
#docker network connect drpg_app $1
