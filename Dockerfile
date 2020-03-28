FROM nvidia/cuda:10.0-base-ubuntu18.04

# Update apt
RUN apt-get -y update

# Install python
RUN apt-get install -y python3.7 \
    python3-pip

# Upgrade pip
RUN pip3 install --no-cache-dir --upgrade pip 

# Install your python libraries
RUN pip3 install --no-cache-dir numpy \
    matplotlib \
    scikit-learn \ 
    pillow \
    requests \
    flask \
    tqdm \
    tensorflow-gpu==1.15 \
    keras

ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get install -y python3-tk
# COPY ./src/ /keras_yolo

# WORKDIR /keras_yolo/src

# EXPOSE 5000

# CMD python3 app.py
