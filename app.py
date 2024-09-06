from dotenv import load_dotenv
load_dotenv() # Initiate the Local Env Variables

from PIL import Image
import google.generativeai as genai
import textwrap
import pathlib
import streamlit as st

# Setup the local environment
import os 
genai.configure(api_key = os.getenv("GOOGLE-API-KEY"))

# Create the Streamlit Front End Page
st.set_page_config("Gemini APP")
st.header("Image Annotation using Gemini Flash")
input = st.text_input("Input Prompt: ", key = "input")

uploaded_file = st.file_uploader(label = "Upload an Image...", type = ["jpeg", "jpg", "png"])


# Let's define the Model and the Image Annotation
def generate_response(input, image):
    model = genai.GenerativeModel("gemini-1.5-flash")
    if input != "":
        response = model.generate_content([input, image])
    else:
        response = model.generate_content(input)
    return(response.text)

# Image Processing
image = ""
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption = "Image Uploaded", use_column_width = True)
    

submit = st.button("Do the Magic")
if submit:
    response = generate_response(input, image)
    st.subheader("Response Generated is ...")
    st.write(response)