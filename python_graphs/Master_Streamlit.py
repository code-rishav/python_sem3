import streamlit as st
import pandas as pd 
import sys
import numpy as np
import re


st.title('Society Analyzer')


@st.cache
def Load_Dataframe_excel(input_file,sheet_name):
    dataframe= pd.read_excel(input_file,sheet_name)
    return dataframe

@st.cache
def Load_Dataframe_csv(input_file):
    dataframe = pd.read_csv(input_file)
    return dataframe


st.subheader('Input Society Dataset')
input_format = st.selectbox('Choose Society',['Excel','CSV'])
input_file = st.file_uploader("Enter a Club or Society")

if input_file is not None:

    if input_format == "Excel":
        excel_file = pd.ExcelFile(input_file,engine='openpyxl')
        data_sheet_selection = st.selectbox("Choose the relevant sheet",excel_file.sheet_names)
        input_dataframe = Load_Dataframe_excel(input_file,data_sheet_selection)
    
    if input_format == 'CSV':
        input_dataframe = Load_Dataframe_csv(input_file)

    st.subheader("Society Summary")
    st.write(input_dataframe.describe())

  