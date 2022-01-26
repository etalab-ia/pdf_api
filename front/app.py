import streamlit as st
import os
from werkzeug.utils import secure_filename
import logging
from pathlib import Path
import ocrmypdf
import zipfile


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

ALLOWED_EXTENSIONS = set(['pdf'])

CWD = Path(os.getcwd())
UPLOAD_DIRECTORY = CWD / "results_OCR"

if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

st.title('OCR my PDF')
uploaded_files = st.file_uploader('Upload your file(s)', accept_multiple_files=True)

#if uploaded_files is not None:
list_pdf = []
list_txt = []

for uploaded_file in uploaded_files:
    filename = uploaded_file.name

    if filename[-3:].lower() in ALLOWED_EXTENSIONS:
        filename = secure_filename(filename) #make sure we have a proper filename
        logger.info(f'**found {filename}')
        full_filename = UPLOAD_DIRECTORY / filename
        ocrmypdf.ocr(uploaded_file, full_filename.with_suffix(".pdf"), sidecar=full_filename.with_suffix('.txt'), l="fra")
        #uploaded_file.seek(0)
        list_pdf.append(full_filename.with_suffix(".pdf"))
        list_txt.append(full_filename.with_suffix(".txt"))

if len(list_txt)==1:
    pdf_to_download = full_filename.with_suffix(".pdf")
    pdf_name = filename
    txt_to_download = full_filename.with_suffix(".txt")
    txt_name = '{}.txt'.format(filename[:-4])

if len(list_txt) > 1:
    pdf_to_download = UPLOAD_DIRECTORY / "folder_pdf.zip"
    pdf_name = "folder_pdf.zip"
    txt_to_download = UPLOAD_DIRECTORY / "folder_txt.zip"
    txt_name = "folder_txt.zip"
    with zipfile.ZipFile(UPLOAD_DIRECTORY / "folder_txt.zip", 'w') as zipMe:
        for file in list_txt:
            zipMe.write(file, os.path.basename(file), compress_type=zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(UPLOAD_DIRECTORY / "folder_pdf.zip", 'w') as zipMe:
        for file in list_pdf:
            zipMe.write(file, os.path.basename(file), compress_type=zipfile.ZIP_DEFLATED)

if len(list_txt) > 0:
    with open(txt_to_download, 'rb') as f:
        st.download_button('Download Txt', f, file_name=txt_name)  # Defaults to 'application/octet-stream'
    with open(pdf_to_download, 'rb') as f:
        st.download_button('Download PDF', f, file_name=pdf_name)

files = [os.path.join(UPLOAD_DIRECTORY, x) for x in os.listdir(UPLOAD_DIRECTORY)]
for f in files:
    print(f)
    os.remove(f)