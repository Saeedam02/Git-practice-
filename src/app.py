import streamlit as st
import pandas as pd
from io import StringIO
import json
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
# from PIL import Image ## it's used for image processing

# st.sidebar.text_input('Enter your username: ')
# st.sidebar.text_input('Enter your password: ')
# st.sidebar.button('login')


#second way to create login:
login_option=st.sidebar.radio('login/sign up',('login','sign up'))

if login_option=='login':
    with st.sidebar.form("Login"):
        st.write("login here")
        username=st.text_input('Username')
        Password=st.text_input('password', type='password')

        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass

else:
    with st.sidebar.form("sign up"):
        st.write("sign up here")
        username=st.text_input('Username')
        Password=st.text_input('password', type='password')
        Email=st.text_input('Email')
        # Every form must have a submit button.
        submitted = st.form_submit_button("Login")
        if submitted:
            pass

        

# banner=Image.open('../data/banner.png')
# st.image('banner')

st.title(':zap: paytopia dashboard')
col1,col2=st.columns(2)
col1.metric(label="pytopia members",value="4000",delta="100")
col2.metric(label="pytopia website members",value="5000",delta="150")


st.text('Hi')

st.code('x=2 , y=5 ,')

try:
    from stringI0 import stringI0 ##for python 2
except ImportError:
    from io import StringIO ## for python 3

    with st.expander('ststistics'):
        fig,ax =plt.subplots(1,1, figsize=(10,5))
        sb.histplot(np.random.randn(100),ax=ax)
        st.pyplot(fig)
with st.expander('User profile'):
    col1,col2=st.columns(2)
    col1.text_input('Name: ')
    col2.text_input('Location: ')
    st.camera_input('camera input',key='camera_input')

# uploaded_file = st.file_uploader("Choose a file")
# if uploaded_file is not None:
#     # To read file as bytes:
#     bytes_data = uploaded_file.getvalue()
#     st.write(bytes_data)

#     # To convert to a string based IO:
#     stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
#     st.write(stringio)

#     # To read file as string:
#     string_data = stringio.read()
#     st.write(string_data)

#     # Can be used wherever a "file-like" object is accepted:
#     dataframe = pd.read_csv(uploaded_file)
#     st.write(dataframe)

#     data=json.loads(string_data)
#     st.json(data)


with st.expander('statistics'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

        data=json.loads(string_data)
        st.json(data)

  