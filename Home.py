import streamlit as st
import pandas as pd
from streamlit_ace import st_ace
from pandasql import sqldf


st.set_page_config(page_title="Learn SQl", page_icon=":bar_chart:", layout="wide", initial_sidebar_state="expanded")

@st.cache
def get_data():
    orders = pd.read_csv('orders.csv')
    users = pd.read_csv('users.csv')

    return orders, users


orders, users = get_data()

query = st_ace(language="sql")

if query:

    try:
        query_res = sqldf(query)
        st.dataframe(query_res)
    except Exception as e:
        st.warning(e)



