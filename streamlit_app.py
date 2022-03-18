import streamlit as st
import keras
import pickle
from keras.optimizers import adam_v2
from keras.preprocessing.image import ImageDataGenerator
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
import tensorflow_hub as hub
import pandas as pd
import re
from PIL import Image
from tensorflow import keras
import os


class AIModel:
    
    def __init__(self):
        with open('./model/tokenizer.pickle', 'rb') as handle:
            self.tokenizer = pickle.load(handle)
        self.model = keras.models.load_model('./model/model.hdf5')
	
    def exec(self, sentences):
        X = self.tokenizer.texts_to_sequences(sentences)
        X = pad_sequences(X, padding='post', maxlen=250)
        return self.model.predict(X)


def load_model(modelfile):
    return 42


st.set_page_config(page_title="AI for Industry", page_icon="", layout='centered', initial_sidebar_state="collapsed")

def main(model):
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Ia for industry </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    st.write(os.walk("/"))
    user_input = st.text_input("label goes here", default_value_goes_here)
    st.write(model.exec([user_input]))

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
#    model = load_model("model.h5")
    model = AIModel()
    main(model)
