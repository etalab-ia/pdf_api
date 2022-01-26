
# PDF Streamlit Application 
This API is part of the Lab IA effort to help administrations to process administrative documents. We are also working a solution that performs OCR and information extraction on documents : [LirIA](https://github.com/etalab-ia/ocr-xtract). Other Lab IA projects can be found at the [Lab IA](https://github.com/etalab-ia).

#### Project Status: [Active]

## Intro/Objectives

The purpose of this repo is to provide a web application that enables you to convert scanned PDF files into a txt file and an editable pdf file. 
You can either upload one PDF at a time or uplaod multiple files at once.

If you upload one PDF file, you will be able to download 
- the corresponding txt file by clicking the "download txt" button 
- the editable PDF file by clicking the "download pdf" button 

If you upload multiple PDF files at a time, you will be able to download: 
- a zip file containing all the corresponding txt files by clicking the "download txt" button 
- a zip file containing all the corresponding editable pdf files by clicking the "download txt" button 

### Methods Used
* OCR 

### Technologies
* Python
* OCRmyPDF
* Docker



## Getting Started
The easiest way to test this application is by using Docker and Docker Compose.

1. Install Docker (https://docs.docker.com/get-docker/)
2. Clone this repo (for help see this [tutorial](https://help.github.com/articles/cloning-a-repository/)).
3. Launch the wrapper bash file `run_docker.sh`. This file will clean and rebuild the required Docker containers by calling `docker-compose.yml`.
4. Go to "http://localhost:8501/"



## Contact
* Feel free to contact [Lab IA](https://github.com/etalab-ia/) team members with any questions or if you are interested in contributing!
