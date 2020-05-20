# use the cuda from lab 1 as the base image
FROM w251/cuda:dev-tx2-4.3_b132

ARG URL=http://169.44.201.108:7002/jetpacks/4.3

RUN apt-get update && apt install -y git pkg-config wget build-essential cmake unzip

WORKDIR /tmp

# Get pip
RUN apt-get update && apt-get install -y     software-properties-common
RUN apt-get update && apt-get install -y python3-pip

# Install PIP and numpy and cython
RUN pip3 install --upgrade pip \
     && pip3 install Cython

# Install the mosquito business
RUN pip3 install paho-mqtt

# Change working directory
WORKDIR /

# Add CUDA to PATH
ENV PATH $PATH:/usr/local/cuda-10.0/bin

#
RUN ldconfig

# Add the python file to the container
ADD gpu_temp.py /

# Run the face detecting python script
CMD python3 gpu_temp.py


