FROM python

RUN apt-get update && apt install -y git pkg-config wget build-essential cmake unzip

# Install the mosquito business
RUN pip install paho-mqtt

# Install s3cmd
RUN pip install --upgrade s3cmd

# Add our python file
ADD catch_and_release.py /

# 

CMD python catch_and_release.py

