import streamlit as st
import pandas as pd
import spatialcsv
import csv

st.set_page_config(layout="wide")



st.subheader("Enter a CSV file to load it onto the map. \n It can be a url or local file, but should have a column with latitude values and a column with longitude values")
st.markdown("Some examples to try out can be found here: [Examples](https://github.com/TJHomer/spatialcsv/tree/main/spatialcsv/example_files)")

col1, col2 = st.columns([4, 1])
okay = False

with col1:

    data = st.text_input(
            "Filepath or url:"
        )

with col2:
    
    if data:
        cols = spatialcsv.get_cols(data)
        val1 = st.selectbox('Choose which column is latitude', cols)
        val2 = st.selectbox('Choose which column is longitude', cols)
        epsg = st.text_input('Enter EPSG number (optional). Deafault is 4326')
        okay = st.button("Enter") 

with col1:
    
    if okay:
        if epsg:
            points = spatialcsv.Points(data, [val1, val2], epsg=epsg)
        else:
            points = spatialcsv.Points(data, [val1, val2])
        l = points.to_streamlit()
        st.map(l)


    st.markdown("App created with python package [spatialcsv](https://pypi.org/project/spatialcsv/). View sourcecode here: [Github](https://github.com/TJHomer/spatialcsv)")
