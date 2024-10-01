FROM continuumio/miniconda:4.7.12

RUN conda install -c forge \
    joblib==0.14.1 \
    bitarray==1.2.0 \
    numpy==1.16.6 \
    pandas==0.24.2 \
    scipy==1.2.1 \
    git==2.32.0

WORKDIR /
RUN git clone --depth 1 https://github.com/JonJala/mtag.git && \
    cd mtag && \
    git reset --hard 9e17f3cf1fbcf57b6bc466daefdc51fd0de3c5dc && \
    rm -rf .git

WORKDIR /mtag

ENTRYPOINT ["/opt/conda/bin/python", "mtag.py"]