import plotly.express as plt
import streamlit as st
import pandas as pd
st.set_page_config(page_title='Data-Visualization',page_icon='Images/brand.png')
data=pd.DataFrame()
def visualization(data):
        col1,col2=st.columns(2)
        chart=col1.selectbox('Choose chart', options=['','Line','Bar','Histogram','Scatter'])
        columns=col2.multiselect('Choose column',options=data.columns)
        try:
            if len(columns)==2:
                if chart=='Line':
                    st.write(plt.line(x=data[columns[0]],y=data[columns[1]]))
                if chart=='Bar':
                    st.write(plt.bar(x=data[columns[0]],y=data[columns[1]]))
                if chart=='Histogram':
                    st.write(plt.histogram(x=data[columns[0]],y=data[columns[1]]))
                if chart=='Scatter':
                    st.write(plt.scatter(x=data[columns[0]],y=data[columns[1]]))
                    
            else:
                if chart=='Line':
                    st.write(plt.line(data[columns]))
                if chart=='Bar':
                    st.write(plt.bar(data[columns]))
                if chart=='Histogram':
                    st.write(plt.histogram(data[columns]))
                if chart=='Scatter':
                    st.write(plt.scatter(data[columns]))
                
        except:
            st.write('Choose correct columns')
st.title('Data-Visualization')
def m():
    try:
        file=st.file_uploader('Choose the file')
        if file is not None:
           try:
                data=pd.read_csv(file)
                visualization(data)
           except:
                try:
                    data=pd.read_excel(file)
                    st.write('If you did not get please try CSV file type')
                    visualization(data)  
                except:
                    st.write('')
    except:
        st.write("Enter CSV or Excel files only")
if __name__=='__main__':
    m()
