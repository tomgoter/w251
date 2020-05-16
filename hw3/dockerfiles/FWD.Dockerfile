FROM alpine

RUN apk update && apk add mosquitto-clients

CMD mosquitto_sub -h mosquitto -t hw3_topic


