FROM ubuntu:24.04

ENV TZ=Europe
ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /tmp
COPY /scripts/apt_get_essential.sh .
RUN bash apt_get_essential.sh && \
    rm apt_get_essential.sh


WORKDIR /tmp
COPY /scripts/install_mambaforge.sh .
RUN bash install_mambaforge.sh
COPY /scripts/environment.yml .
RUN mamba env update --name base --file environment.yml && \
    conda clean --all --yes && \
    rm -rf /tmp/*

WORKDIR /home
