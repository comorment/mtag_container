FROM continuumio/miniconda:latest

RUN conda install -c forge \
    joblib==0.14.1 \
    bitarray==1.2.0 \
    numpy==1.16.6 \
    pandas==0.24.2 \
    scipy==1.2.1

WORKDIR /
RUN conda install git -y
RUN git clone https://github.com/JonJala/mtag.git
WORKDIR /mtag

ENTRYPOINT ["/opt/conda/bin/python", "mtag.py"]