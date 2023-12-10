import streamlit as st
import requests

api_key = 'E5P8rxeF1fV5cG0IBD0uQCcoISdxmh8QSwMbbz7I'
api = f' https://api.nasa.gov/planetary/earth/assets?api_key={api_key}'

req = requests.get(api)
df = req.json()

title = df['title']
date = df['date']
data = df['explanation']
image = df['url']

response1 = requests.get(image)
with open('image.jpg','wb') as file:
    file.write(response1.content)

st.title(title)
st.subheader(date)
st.image('image.jpg')
st.info(data)

# Social media links
st.markdown(
    """
    <style>
    .social-media {
        display: flex;
        justify-content: center;
        align-items: center;
        margin-top: 50px;
    }
    .social-media a {
        margin: 0 30px;
        text-decoration: none;
        color: #4a4a4a;
    }
    </style>
    """
    , unsafe_allow_html=True)
st.markdown(
    """
    <head>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
    </head>
    """
    , unsafe_allow_html=True)

st.markdown(
    """
    <div class="social-media">
        <a href="https://www.twitter.com/krshxcx"><i class="fab fa-twitter"></i></a>
        <a href="https://github.com/krshxcx"><i class="fab fa-github"></i></a>
        <a href="https://www.instagram.com/krshxcx"><i class="fab fa-instagram"></i></a>
        <a href="https://www.linkedin.com/in/saikrishna-durgam/"><i class="fab fa-linkedin"></i></a>
    </div>
    """
    , unsafe_allow_html=True)
                
