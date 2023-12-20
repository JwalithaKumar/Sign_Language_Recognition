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
    fp = "./Sign_Language/action.h5"
    model_loader = load_model(fp)
    return model_loader


cnn = loading_model()
st.write("""
# Online Sign Language Recognition
""")


temp = st.file_uploader("Please Provide the Snap Shot of your Sign")
