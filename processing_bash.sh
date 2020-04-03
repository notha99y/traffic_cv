cont_id=`docker ps | grep notha99y | cut -d' ' -f1`
echo "Bashing into processing (container id: $cont_id)" 
docker exec -it $cont_id bash && cd /workspace