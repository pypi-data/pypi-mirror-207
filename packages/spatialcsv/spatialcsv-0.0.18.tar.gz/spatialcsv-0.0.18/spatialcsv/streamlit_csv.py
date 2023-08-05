import streamlit as st
import pandas as pd
import spatialcsv
import csv

st.set_page_config(layout="wide")



st.title("Load any csv into a map")


col1, col2 = st.columns([4, 1])
okay = False

with col1:

    data = st.text_input(
            "Enter a filepath or url of a csv:"
        )

with col2:
    
    if data:
        cols = spatialcsv.get_cols(data)
        val1 = st.selectbox('Choose which column is latitude', cols)
        val2 = st.selectbox('Choose which column is longitude', cols)
        okay = st.button("Enter") 

with col1:
    
    if okay:
        points = spatialcsv.Points(data, [val1, val2],)
        l = points.to_streamlit()
        st.map(l)


