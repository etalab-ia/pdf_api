FROM continuumio/miniconda3

RUN mkdir -p /usr/share/man/man1/

RUN apt-get -y update
RUN apt-get -y install \
    g++ \
    build-essential \
    ocrmypdf \
    libpoppler-cpp-dev \
    pkg-config \
    openjdk-11-jdk \
    ghostscript \
    icc-profiles-free \
    liblept5 \
    libxml2 \
    pngquant \
    qpdf \
    tesseract-ocr \
    tesseract-ocr-fra \
    zlib1g


ADD environment.yml environment.yml

RUN conda env create -f environment.yml
ENV PATH /opt/conda/envs/pdf_api/bin:$PATH
RUN /bin/bash -c "source activate pdf_api"
COPY . .
CMD [ "streamlit", "run", "app.py", "--server.enableCORS=false", "--server.enableXsrfProtection=false","--server.enableWebsocketCompression=false" ]