import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression,LogisticRegression
from sklearn.preprocessing import LabelEncoder
st.set_page_config(page_title='Data Prediction')
data=pd.DataFrame()
def split_data(data):
        global xtr,xtes,ytr,ytes
        xtr,xtes,ytr,ytes=train_test_split(data[features],data[target])
def num_cat_columns(data):
        global cat_col,num_col
        num_col=data.select_dtypes(include=['int64','float64'])
        cat_col=data.select_dtypes(exclude=['int64','float64'])
def cat_convert(data):
        le=LabelEncoder()
        for i in cat_col:
            data[i]=le.fit_transform(data[i])
def features_target(data):
        col1,col2=st.columns(2)
        global features,target
        features=col1.multiselect('Choose features',options=data.columns)
        target=col2.selectbox('Choose target',options=data.columns)
def algo(data):
        if data.isnull().sum().sum()==0:
            model=st.selectbox('Choose model',options=['','Linear Regression','Logistic Regression'])
            ml_class.num_cat_columns(data)
            ml_class.cat_convert(data)
            ml_class.features_target(data)
            ml_class.split_data(data)
            if st.button('predict'):
                if len(features)>0 and len(target)==1:
                    if model=='Linear Regression':
                            lr=LinearRegression().fit(xtr,ytr)
                            st.write(lr.score(xtes,ytes))
                    if model=='Logistic Regression':
                        logreg=LogisticRegression().fit(xtr,ytr)
                        st.write(logreg.score(xtes,ytes))

        else:
            st.warning('Please deal with missing values and come again')
st.write('Data Prediction')
def m():
    try:
        file=st.file_uploader('Choose the file')
        if file is not None:
           try:
                data=pd.read_csv(file)
                algo(data)
           except:
                try:
                    data=pd.read_excel(file)
                    st.write('If you did not get report please try CSV file type')
                    algo(data)
                except:
                    st.write('')
    except:
        st.write("Enter CSV or Excel files only please try again")
if __name__=='__main__':
    m()
