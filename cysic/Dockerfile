FROM ubuntu:22.04
RUN apt-get update  && \
    apt-get install -y \
    htop \
    curl \
    && apt-get clean &&\
    rm -rf /var/lib/apt/lists/*

WORKDIR /root

ENTRYPOINT cd /root && bash start.sh
