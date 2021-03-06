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

RUN apt-get clean && rm -rf /tmp/* /var/tmp/* /var/lib/apt/lists/* && apt-get -y autoremove

# hbase connector
RUN pip3 install --no-cache-dir happybase