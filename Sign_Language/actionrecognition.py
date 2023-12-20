import streamlit as st
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
import tensorflow as tf

from tempfile import NamedTemporaryFile
from tensorflow.keras.preprocessing import image

#st.set_option('deprecation.showfileUploaderEncoding', False)


@st.cache(allow_output_mutation=True)
def loading_model():
    fp = "./model/BrainTumorCheck.h5"
    model_loader = load_model(fp)
    return model_loader


cnn = loading_model()
st.write("""
# Cloud Based Web Application Tuberculosis Detection Using CNN App
Built by Jayes and Team
""")


temp = st.file_uploader("Please Provide the Snap Shot of your X-Ray Image")