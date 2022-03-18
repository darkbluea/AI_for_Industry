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
#    resnet50_url = 'https://tfhub.dev/google/imagenet/resnet_v2_50/feature_vector/5'
#    feature_extractor_layer = hub.KerasLayer(resnet50_url,
#                                               trainable=False, # freeze the underlying patterns
#                                               name='feature_extraction_layer',
#                                               input_shape=(224, 224)+(3,)) # define the input image shap
#
#    resnet_model2 = keras.Sequential([
#        feature_extractor_layer,
#        keras.layers.BatchNormalization(),
#        keras.layers.Dropout(0.2),
#        keras.layers.Dense(1, activation = 'sigmoid'),
#    ])
#
#    metrics = ['accuracy', keras.metrics.AUC(), keras.metrics.Recall()]
#
#    resnet_model2.compile(loss='binary_crossentropy',
#                            metrics = [metrics],
#                            optimizer = adam_v2.Adam(learning_rate = 5e-4))
#
#    resnet_model2.load_weights(modelfile)
#    return resnet_model2


st.set_page_config(page_title="AI for Industry", page_icon="", layout='centered', initial_sidebar_state="collapsed")

def main(model):
    html_temp = """
    <div>
    <h1 style="color:MEDIUMSEAGREEN;text-align:left;"> Neural Network prediction on patient lungs </h1>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

if __name__ == '__main__':
	model = load_model("model.h5")
	main(model)
