# Applying CV on Singapore Traffic images

## Useful links
- [api](https://data.gov.sg/dataset/traffic-images?view_id=a0e54baf-6ef7-4bca-9aa2-8c6ca37a0a0e&resource_id=e127e29a-bd48-47e2-a0a7-e89ce31f10c7)
- [map of cameras](https://data.gov.sg/dataset/traffic-images?view_id=39ba8de0-6242-40d3-8664-793316c47b09&resource_id=e127e29a-bd48-47e2-a0a7-e89ce31f10c7)
- [writing to hbase](https://gist.github.com/jarrettmeyer/26b3e1fcd423071a7a6d)
- [writing to hdfs](https://creativedata.atlassian.net/wiki/spaces/SAP/pages/61177860/Python+-+Read+Write+files+from+HDFS)

## How to run
### Car Detector
1. Download darknet weights [here](https://pjreddie.com/darknet/yolo/)
1. Convert them to `.h5` file ```python convert.py yolov3.cfg yolov3.weights model_data/yolo.h5 ``` 
1. build Docker Image ```docker build . -t notha99y/keras_yolo_dev```
1. Run the container ```./run_docker.sh``` you might need to ```chmod +x run_docker.sh```
### Cloudera docker
1. Get docker image ```docker pull cloudera/quickstart:latest```
1. Run it ```docker run --hostname=quickstart.cloudera --privileged=true -it -p 7180:7180 -p 8888:8888 cloudera/quickstart:latest /usr/bin/docker-quickstart```
1. Access hue and cloudera manager with ports 7180 and 8888 respectively
