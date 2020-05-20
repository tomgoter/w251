FROM alpine

RUN apk update && apk add mosquitto-clients

RUN apk add python3

RUN apk add py3-pip

RUN pip3 install paho-mqtt

ADD catch.py /

CMD python3 catch.py


