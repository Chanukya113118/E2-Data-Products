import pandas as pd
import streamlit as st
import plotly.express as plt
st.set_page_config(page_title='Data Anlysis')
data=pd.DataFrame()
def analyse_fun(data):
        data=data
        col1,col2=st.columns(2)
        if col1.button('Describe'):
            st.write(data.describe())
        if col2.button('Missing value Information'):
            st.write(data.isnull().sum())
        if col1.button('Correlation Values'):
            st.write(data.corr())
        st.button("Press")
def m():
    try:
        file=st.file_uploader('Choose the file')
        if file is not None:
           try:
                data=pd.read_csv(file)
                analyse_fun(data)
           except:
                try:
                    data=pd.read_excel(file)
                    st.write('If you did not get report please try CSV file type')
                    analyse_fun(data)  
                except:
                    st.write('')
    except:
        st.write("Enter CSV or Excel files only")
if __name__=='__main__':
    m()
