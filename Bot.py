#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import openai
from dotenv import load_dotenv, find_dotenv

import streamlit as st
import os
from PIL import Image
from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

#openai.api_key = os.environ["OPENAI_API_KEY"]


# In[2]:



def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


# In[3]:


context = [{'role': 'system', 'content': """
You are MlChatGenius, an automated service to explain topics related to Data Science and Machine Learning. \
You first greet the user, then say, "I am here to assist you".\
you then respond as a Data Science expert. \
You explain and then summarize it in short, giving real-life examples. \
You should respond in a short, very conversational, similar to Andrew Ng.
"""}]

def collect_messages(prompt):
    response = get_completion_from_messages(context + [{'role': 'user', 'content': prompt}])
    context.append({'role': 'user', 'content': prompt})
    context.append({'role': 'assistant', 'content': response})
    return response

def main():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    # Custom CSS styling for the chatbox and background color
    custom_css = """
    <style>
    body {
        background-color: lightblue; /* Change the background color here */
    }
    .title {
        color: #0492C2; /* Change the color code here */
        font-size: 38px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    div.stTextInput > div > div {
        background-color: #F6F6F6;
        color: black;
        padding: 0.75rem;
        border-radius: 0.5rem;
        }
    button.stButton {
        background-color: #3366CC;
        color: white;
        border-radius: 0.5rem;
        padding: 0.5rem 1rem;
        font-size: 1rem;
    }
    div.stTextArea > div > textarea {
        background-color: #F6F6F6;
        color: black;
        border-radius: 0.5rem;
        padding: 0.75rem;
    }
    </style>
    """

    # Apply the custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)
    
    st.title("MlChatGenius: Data Science and ML Chatbot")
    image=Image.open("friendly-chatbot.jpg")
    st.image(image)
    st.write("I am a MlChatGenius, an automated service to explain topics related to Data Science and Machine Learning.")
    
    user_input = st.text_input("You:")
    if st.button("Chat!"):
        bot_response = collect_messages(user_input)
        st.write("Assistant:", bot_response)
        


if __name__ == "__main__":
    main()


# In[ ]:




