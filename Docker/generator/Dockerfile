FROM debian:bullseye

WORKDIR /gen

RUN apt-get update && apt-get install -y mosquitto-clients

COPY gen.py /gen/gen.py

ENTRYPOINT ["/gen/gen.py"]
CMD [ "python3", "gen.py"]

