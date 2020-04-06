cont_id=`docker ps | grep cloudera | cut -d' ' -f1`
echo "Bashing into cloudera (container id: $cont_id)" 
docker exec -it $cont_id bash && cd /workspace