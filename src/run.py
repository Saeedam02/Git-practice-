import streamlit as st
import pandas as pd
from io import StringIO
import json
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
st.title(':zap: paytopia dashboard')
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

# st.camera_input('camera input',key='camera_input')

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
