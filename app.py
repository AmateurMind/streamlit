#import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image








# Display the image with a caption in Streamlit

st.set_page_config(page_title="my webpage",page_icon=":tada:",layout="wide")

def load_lottieurl(url):
    r=requests.get(url)
    if r.status_code!=200:
        return None
    return r.json()

#---load asset---
lottie_coding=load_lottieurl("https://lottie.host/48ddc748-2926-4599-b9eb-52cd7e2fd876/QTHpWP3EsO.json")
img_contact_form=Image.open("img\\brain.jpg")
img_lottie_animation=Image.open("img\\cat.jpg")

with st.container():
    st.subheader("Hi :wave:")
    st.title("This is the official page of Trade Planet🌏")
    st.write("Thhis is just a weird webpage. I don't know why I am making this, I am not a trader LOLzz. My main purpose is to make a webapp and stuff!💻 ")
    st.write("If you are still interested in Trading")
    st.write("I know a webpage for you 🫵")
    st.write("[Instagram link >](https://www.instagram.com/trade_.planet?utm_source=ig_web_button_share_sheet&igsh=ZDNlZDc0MzIxNw==)") 

with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do❔")  
        st.write("##")
        st.write("-Sooo I am an engg student and I am bored.")
        st.write("-Why am I bored.")
        st.write("-Well coz I don't have anything to do.")
        st.write("-Why don't I have anything to do.")   
        st.write("-Because I am not interested in anything and I just wanna sleep rn 🥱.")
        st.write("-Hmmmm ok that's not good.")
        st.write("-yeah.")    
        st.write("-sooooo")    
        st.write("-how long are we gonna talk.")   
        st.write("-idk why is he writing all these things 🙄.")   
        st.write("-{author :brain:}:Well I had to intervene, sorry for that but I was enjoying your sweet talks.")    
        st.write("-....")
        st.write("-{author :brain:}:ohhh i accidentlly deleted them.") 
    with right_column:
        st_lottie(lottie_coding,height=300,key="coding")

#---Projects
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")

    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("Duhh Nothing To See Here... This Is Subheader Area😒")
        st.write(
            """Hey I found a website where you will get to know about human brain, love etcetera etcetera\n
               Ps-Basically answer to life,the universe, and everthing🤫
              """
        )
        st.markdown("[Here it is](https://www.youtube.com/watch?v=xvFZjo5PgG0)") 

with st.container():
    image_column, text_column=st.columns((1,2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Classy cat")
        st.write("🥰")
        





#st.balloons()



            
            
             
            
        