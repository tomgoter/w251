FROM alpine
# install mosquitto
RUN apk update && apk add mosquitto-clients
# run mosquitto
CMD mosquitto_sub -h mosquitto -t mosquitto
