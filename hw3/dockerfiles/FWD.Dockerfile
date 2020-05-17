FROM alpine

RUN apk update && apk add mosquitto-clients

RUN apk add python

RUN apk add py-pip

RUN pip install paho-mqtt

ADD forward.py /

CMD python forward.py


