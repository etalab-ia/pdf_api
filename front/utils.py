import os
import streamlit as st

def save_uploaded_file(uploaded_file, path):
    with open(os.path.join(path, uploaded_file.name), "wb") as f:
        f.write(uploaded_file.getbuffer())
    return st.success("Saved File:{} to {}".format(uploaded_file.name, path))