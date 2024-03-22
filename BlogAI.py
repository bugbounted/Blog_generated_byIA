import streamlit as st
import google.generativeai as genai
from apikey import google_gemini_api_key, api_key
from openai import OpenAI
client = OpenAI()

#set the application to wide mode
st.set_page_config(layout="wide")

genai.configure(api_key=google_gemini_api_key)

# Set up the model
generation_config = {
  "temperature": 0.9,
  "top_p": 1,
  "top_k": 1,
  "max_output_tokens": 2048,
}

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
]
#setting up our model
model = genai.GenerativeModel(model_name= "gemini-1.0-pro",
                              generation_config = generation_config,
                              safety_settings= safety_settings)


# Sidebar elements
with st.sidebar:
    st.title("Blog Sidebar")
    blog_title = st.text_input("Enter your Blog title")
    keywords = st.text_area("Enter your keywords {between the keywords put comma}")
    nb_words = st.slider("Number of words : ", min_value=200, max_value=10000,step= 200)
    nb_img = st.number_input(" Number of images : ", min_value= 1 , max_value=10, step=1)

    prompt_parts = [
        f" generate a comprehensive, relevant blog post based on a given \"{blog_title}\" and \"{keywords}\". The blog should be approximately {nb_words} words in lenght and suitable for online audiance."
    ]

    button_gen = st.button('Generate Blog')


# Main content area
st.title("Your Blog Intelligent Assistant")
st.subheader("This web App provide you an intelligent assistant that can create for you a blog content based on your keywords")

img_ response = client.images.generate(
        model="dall-e-3",
        prompt="a white siamese cat",
        size="1024x1024",
        quality="standard",
        n=1,
    )

# Display blog posts (replace with your actual content)

#st.write("This is the content of the first blog post.")
if button_gen:
    st.markdown(f"## {blog_title}")
    response = model.generate_content(prompt_parts)
    st.write(response.text)
    img_response =
    (img_response.data[0].url)






