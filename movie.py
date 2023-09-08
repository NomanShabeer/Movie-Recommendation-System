import streamlit as st
import pickle
import pandas as  pd
movies_list=pickle.load(open('moviesdic.pkl','rt'))
movies=pd.DataFrame(movies_list)

st.title("Movie Recommender System")
option = st.selectbox(
'How would you like to be contacted?',
movies['title'].values)

