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
    user_input = st.text_input("Input the text here:", "What a wonderful day! <3")
    result = model.exec([user_input])[0][0]
    st.write("predicted to be : " + str(result) + " (0 being bad, 1 being good)")
    polarity = "good" if result > 0.66 else ("bad" if result < 0.33 else "neutral")
    st.write("prediction is : " + polarity)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
#    model = load_model("model.h5")

#    st.write([(x[0], x[1], x[2]) for x in os.walk(".")])
    model = AIModel()
    main(model)
