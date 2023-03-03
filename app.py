import openai 
from constants import * 
from PIL import Image
import streamlit as st

def word_maker(word_a,word_b):
    return openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[
            {"role": "system", "content": "You are a word maker. You are creative, funny, assertive."},
            {"role": "user", "content": "Combine the word "+word_a+" and the word  "+word_b},
            {"role": "assistant", "content": "Then you explain the meaning of this made up word."},
            {"role": "user", "content": "What does it mean?"}
        ]
    )['choices'][0]['message']['content']


if __name__=='__main__':
    openai.api_key = OPENAI_KEY
    image = Image.open('NameMakerImage.jpeg')
    st.image(image, caption='Photo by Brett Jordan on Unsplash')
    st.header("Write two different words")
    st.subheader('First word here: :point_down:')
    text = st.text_input("Type here")
    st.subheader('Second word here: :point_down:')
    text2 = st.text_input("Type here", key = "last_name")
    while text!='' and text2!='':
        made_up_word_explained = word_maker(text,text2)
        #text_res = st.write('Result='+made_up_word_explained)
        st.markdown("""
        <style>
        .big-font {
            font-size:32px !important;
        }
        </style>
        """, unsafe_allow_html=True)
        st.markdown('<p class="big-font">'+made_up_word_explained+'</p>', unsafe_allow_html=True)
        break
    